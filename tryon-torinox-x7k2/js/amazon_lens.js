// Amazonの試着のレンズの描き方を再現する（2026-10-26 入稿済みMOTION黒の実画面で実測）
// Amazonは「画面に出す明るさの値（sRGB）どうしの掛け算」：表示＝裏の映像 × レンズの色（sRGB値/255）。反射なし。
// three.js は sRGB に変換してからフレームバッファに書くので、乗算ブレンドで同じ計算になる。
// 透過が1未満のレンズ（ミラーB案など）は、透過分を掛け算・残りを照明で照らした色として足す。
// レンズの表面・裏面が重なって2回掛からないよう、ステンシルで1画素1回に制限する。
import * as THREE from 'three';
export function amazonLens(root){
  const extra = [];
  root.traverse(o => {
    if (!o.isMesh || !(o.material.name || '').startsWith('LensMat')) return;
    const m = o.material, t = (m.transmission !== undefined ? m.transmission : 1), map = m.map;
    const mul = new THREE.MeshBasicMaterial({ map, color: new THREE.Color(t, t, t), blending: THREE.MultiplyBlending, premultipliedAlpha: true,
      transparent: true, depthWrite: false, side: THREE.DoubleSide,
      stencilWrite: true, stencilRef: 1, stencilFunc: THREE.NotEqualStencilFunc, stencilZPass: THREE.ReplaceStencilOp });
    mul.name = m.name; o.material = mul; o.renderOrder = 3;
    if (t < 0.999) {
      const lit = new THREE.MeshLambertMaterial({ map, color: new THREE.Color(1 - t, 1 - t, 1 - t), blending: THREE.AdditiveBlending,
        transparent: true, depthWrite: false, side: THREE.DoubleSide,
        stencilWrite: true, stencilRef: 2, stencilFunc: THREE.NotEqualStencilFunc, stencilZPass: THREE.ReplaceStencilOp });
      const o2 = new THREE.Mesh(o.geometry, lit); o2.renderOrder = 4; extra.push([o, o2]);
    }
  });
  extra.forEach(([o, o2]) => o.add(o2));
}
