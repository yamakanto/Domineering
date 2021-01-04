from domineering.DomineeringGame import DomineeringGame
from domineering.human_player import HumanPlayer
from domineering.first_choice_ai import FirstChoiceAI
from domineering.strategy_ai import StrategyAI
from domineering.possible_moves_evaluation import PossibleMovesEvaluation
from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation
from domineering.possible_moves_safe_moves_evaluation import SafeRealPossibleMovesEvaluation
import cProfile


def start_game():
    player1 = HumanPlayer(True)
    player1 = FirstChoiceAI(True)
    player2 = FirstChoiceAI(False)
    #strategy1 = PossibleMovesStrategy(True)
    eval1 = PossibleMovesEvaluation()
    eval2 = RealPossibleMovesEvaluation()
    eval2 = SafeRealPossibleMovesEvaluation()
    player1 = StrategyAI(True, eval2, 2)

    player2 = StrategyAI(False, eval2, 2)
    game = DomineeringGame(5, player1, player2)
    game.play()


if __name__ == '__main__':
    do_profiling = False
    if do_profiling:
        with cProfile.Profile() as pr:
            start_game()
        pr.print_stats()
    else:
        start_game()