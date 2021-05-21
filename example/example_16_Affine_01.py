import king

king.affine(king.circle(king.point(5, 0), 3), lambda x, y: [x * y, x + y])
