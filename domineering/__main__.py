from domineering.DomineeringGame import DomineeringGame
from domineering.human_player import HumanPlayer
from domineering.first_choice_ai import FirstChoiceAI
from domineering.strategy_ai import StrategyAI
from domineering.possible_moves_evaluation import PossibleMovesEvaluation
from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation
from domineering.safe_real_possible_moves_evaluation import SafeRealPossibleMovesEvaluation
from domineering.lookahead_depth import ProgressiveLookaheadDepth
import cProfile
from pstats import Stats
from time import perf_counter


def start_game():
    player1 = HumanPlayer(True)
    player1 = FirstChoiceAI(True)
    player2 = FirstChoiceAI(False)
    #strategy1 = PossibleMovesStrategy(True)
    eval1 = PossibleMovesEvaluation()
    eval2 = RealPossibleMovesEvaluation()
    eval2 = SafeRealPossibleMovesEvaluation()
    lookahead_func = ProgressiveLookaheadDepth([1, 2, 3], [0, 15, 30])
    player1 = StrategyAI(True, eval2, lookahead_func)

    player2 = StrategyAI(False, eval2, lookahead_func)
    game = DomineeringGame(5, player1, player2)
    # game._play_turn()
    game.play()


if __name__ == '__main__':
    do_profiling = True
    if do_profiling:
        with cProfile.Profile() as pr:
            start_game()

        with open('profiling_stats.txt', 'w') as stream:
            stats = Stats(pr, stream=stream)
            stats.strip_dirs()
            stats.sort_stats()
            stats.dump_stats('.prof_stats')
            stats.print_stats()
    else:
        start_time = perf_counter()
        start_game()
        end_time = perf_counter()
        print(f'Finished after {end_time-start_time}.')
