from dataflow_animation.enums import MovementStatus, Path


def is_stay_status(status: MovementStatus) -> bool:
    return status == MovementStatus.INITIAL or status == MovementStatus.STOPPED


def get_linear_path_next_status(
    current_status: MovementStatus,
) -> MovementStatus:
    if current_status == MovementStatus.INITIAL:
        return MovementStatus.MOVING

    if current_status == MovementStatus.MOVING:
        return MovementStatus.STOPPED

    return MovementStatus.FINISHED


def get_next_status(
    current_status: MovementStatus,
    path: Path,
) -> MovementStatus:
    if path == Path.LINEAR:
        return get_linear_path_next_status(current_status)
