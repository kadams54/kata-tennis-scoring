import { start, Player, Score } from "../src/game";

describe("Game state", () => {
  describe("#start", () => {
    it("should have both scores set to love and no winner", () => {
      const game = start();
      expect(game.scores[Player.ONE]).toBe(Score.LOVE);
      expect(game.scores[Player.TWO]).toBe(Score.LOVE);
      expect(game.winner).toBe(null);
    });
  });
});
