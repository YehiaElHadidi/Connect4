from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 570 + 10
TOP = 200 + 35
RIGHT = 1350 - 10
BOTTOM = 875

EMPTY = 0
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
PLAYER_PIECE = 1
COMPUTER_PIECE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]

    def get_board(self):
        return self.board

    def print_grid(self, grid):
        print('#' * 20)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == PLAYER_PIECE:
                    print("R", end=" \t")
                elif grid[i][j] == COMPUTER_PIECE:
                    print("B", end=" \t")
            print("\n")
        print('#' * 20)
        print('\n')

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = PLAYER_PIECE
                elif grid[i][j][0] > 50:
                    grid[i][j] = COMPUTER_PIECE
        return grid

    def _get_grid_cordinates(self):
        startCord = (54, 45)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 110
                y = startCord[1] + j * 108
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        cropedImage = cropedImage.convert("RGB")
        # cropedImage.save("board.png")
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        coordinates = self._get_grid_cordinates()
        pyautogui.click(
            coordinates[column * 6][0] + LEFT,
            coordinates[column * 6][1] + TOP,
        )

    def is_valid_location(self, column):
        return self.board[0][column] == EMPTY

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def get_next_open_row(self, column):
        for r in range(ROW_COUNT - 1, -1, -1):
            if self.board[r][column] == EMPTY:
                return r

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece
