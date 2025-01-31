def temp_in_an_hour(t_room, t_cond, mode):
    if (
        mode == "fan"
        or (mode == "freeze" and t_room <= t_cond)
        or (mode == "heat" and t_room >= t_cond)
    ):
        return t_room
    return t_cond


def main():
    t_r, t_c = map(int, input().split())
    print(temp_in_an_hour(t_r, t_c, input()))


if __name__ == "__main__":
    main()
