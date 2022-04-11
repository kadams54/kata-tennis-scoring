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

  describe("#nextScore", () => {
    it("should advance a player's score to the next point value", () => {
      expect(nextScore(Score.LOVE)).toBe(Score.FIFTEEN);
      expect(nextScore(Score.FIFTEEN)).toBe(Score.THIRTY);
      expect(nextScore(Score.THIRTY)).toBe(Score.FOURTY);
      expect(nextScore(Score.FOURTY)).toBe(Score.WINNER);
    });
  });
});
