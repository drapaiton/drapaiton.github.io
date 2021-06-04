import { PUSH_MESSAGE } from "./constants";

export default (state, action) => {
  const { payload, type } = action;

  switch (type) {
    case PUSH_MESSAGE:
      return {
        ...state,
        messages: [...state.messages, payload],
      };
    default:
      return state;
  }
};
