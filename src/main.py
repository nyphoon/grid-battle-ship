import argparse
import json

import game
import visual

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('code', type=str)
    parser.add_argument('-i', '--image', action='store_true')
    parser.add_argument('-p', '--preview', action='store_true')
    parser.add_argument('-j', '--use-json', action='store_true')
    args = parser.parse_args()

    if args.use_json:
        with open(args.code) as f:
            code = json.load(f)
    else:
        code_parts = args.code.split('-')
        code = {'N': int(code_parts[0]),  # grid size NxN
                'S': code_parts[1],  # Ships
                'T': code_parts[2]}  # Attacks

    ships = game.create_ships(code['S'])
    attacks = game.create_attacks(code['T'])
    result = game.eval_game(ships, attacks)
    print(result)

    if args.image or args.preview:
        image = visual.draw_game((code['N'], code['N']), ships, attacks)

    if args.image:
        image.save('grid_battle_ship.jpg', quality=95)

    if args.preview:
        visual.show_image(image)
