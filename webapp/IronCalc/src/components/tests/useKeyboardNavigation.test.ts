import type { KeyboardEvent as ReactKeyboardEvent, RefObject } from "react";
import { expect, test, vi } from "vitest";
import {
  handleKeyboardNavigation,
  type KeyboardNavigationOptions,
} from "../Workbook/useKeyboardNavigation";

const createHarness = () => {
  const root = {} as HTMLDivElement;
  const callbacks = {
    onCellsDeleted: vi.fn(),
    onSelectAll: vi.fn(),
    onExpandAreaSelectedKeyboard: vi.fn(),
    onExpandAreaSelectedKeyboardToEdge: vi.fn(),
    onEditKeyPressStart: vi.fn(),
    onCellEditStart: vi.fn(),
    onBold: vi.fn(),
    onItalic: vi.fn(),
    onUnderline: vi.fn(),
    onNavigationToEdge: vi.fn(),
    onPageDown: vi.fn(),
    onPageUp: vi.fn(),
    onArrowDown: vi.fn(),
    onArrowUp: vi.fn(),
    onArrowLeft: vi.fn(),
    onArrowRight: vi.fn(),
    onKeyHome: vi.fn(),
    onKeyEnd: vi.fn(),
    onUndo: vi.fn(),
    onRedo: vi.fn(),
    onNextSheet: vi.fn(),
    onPreviousSheet: vi.fn(),
    onEscape: vi.fn(),
    onSelectColumn: vi.fn(),
    onSelectRow: vi.fn(),
  };
  const options: KeyboardNavigationOptions = {
    ...callbacks,
    root: { current: root } as RefObject<HTMLDivElement>,
  };
  const createEvent = (overrides: Partial<ReactKeyboardEvent> = {}) => {
    const stopPropagation = vi.fn();
    const preventDefault = vi.fn();
    const event = {
      key: "",
      ctrlKey: false,
      metaKey: false,
      shiftKey: false,
      altKey: false,
      target: root,
      stopPropagation,
      preventDefault,
      ...overrides,
    } as ReactKeyboardEvent;
    return { event, stopPropagation, preventDefault };
  };
  return { callbacks, options, root, createEvent };
};

test("Ctrl+A selects all", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "a",
    ctrlKey: true,
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onSelectAll).toHaveBeenCalledOnce();
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("Ctrl+Shift+ArrowRight expands selection to edge", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "ArrowRight",
    ctrlKey: true,
    shiftKey: true,
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onExpandAreaSelectedKeyboardToEdge).toHaveBeenCalledWith(
    "ArrowRight",
  );
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("Cmd+Shift+Home expands selection to Home edge", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "Home",
    metaKey: true,
    shiftKey: true,
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onExpandAreaSelectedKeyboardToEdge).toHaveBeenCalledWith(
    "Home",
  );
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("Ctrl+Shift+End expands selection to End edge", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "End",
    ctrlKey: true,
    shiftKey: true,
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onExpandAreaSelectedKeyboardToEdge).toHaveBeenCalledWith(
    "End",
  );
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("Delete clears selected cells", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "Delete",
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onCellsDeleted).toHaveBeenCalledOnce();
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("Backspace clears selected cells", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "Backspace",
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onCellsDeleted).toHaveBeenCalledOnce();
  expect(stopPropagation).toHaveBeenCalledOnce();
  expect(preventDefault).toHaveBeenCalledOnce();
});

test("ignores keys when event target is outside workbook root", () => {
  const { callbacks, options, createEvent } = createHarness();
  const { event, stopPropagation, preventDefault } = createEvent({
    key: "a",
    ctrlKey: true,
    target: {} as HTMLDivElement,
  });

  handleKeyboardNavigation(event, options);

  expect(callbacks.onSelectAll).not.toHaveBeenCalled();
  expect(stopPropagation).not.toHaveBeenCalled();
  expect(preventDefault).not.toHaveBeenCalled();
});
