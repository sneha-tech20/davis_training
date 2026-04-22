import geometry3d as g

def main():
    print("Select a figure:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")

    choice = int(input("Enter your choice: "))

    print("\nSelect operation:")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")

    op = int(input("Enter operation: "))

    if choice == 1:
        a = float(input("Enter side: "))
        if op == 1:
            print("CSA =", g.cube_csa(a))
        elif op == 2:
            print("TSA =", g.cube_tsa(a))
        elif op == 3:
            print("Volume =", g.cube_volume(a))

    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        if op == 1:
            print("CSA =", g.cuboid_csa(l, b, h))
        elif op == 2:
            print("TSA =", g.cuboid_tsa(l, b, h))
        elif op == 3:
            print("Volume =", g.cuboid_volume(l, b, h))

    elif choice == 3:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        if op == 1:
            print("CSA =", g.cylinder_csa(r, h))
        elif op == 2:
            print("TSA =", g.cylinder_tsa(r, h))
        elif op == 3:
            print("Volume =", g.cylinder_volume(r, h))

    elif choice == 4:
        r = float(input("Enter radius: "))
        if op == 1 or op == 2:
            l = float(input("Enter slant height: "))
        if op == 3:
            h = float(input("Enter height: "))

        if op == 1:
            print("CSA =", g.cone_csa(r, l))
        elif op == 2:
            print("TSA =", g.cone_tsa(r, l))
        elif op == 3:
            print("Volume =", g.cone_volume(r, h))

    elif choice == 5:
        r = float(input("Enter radius: "))
        if op == 1:
            print("CSA =", g.sphere_csa(r))
        elif op == 2:
            print("TSA =", g.sphere_tsa(r))
        elif op == 3:
            print("Volume =", g.sphere_volume(r))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()