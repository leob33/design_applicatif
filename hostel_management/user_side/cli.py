from hostel_management.domain.model.price import Price
from hostel_management.domain.use_cases.modify_hostel_room_prices_use_case import ModifyHostelRoomPricesUseCase
from hostel_management.repository.hostel_repository_hard_coded import HotelRepositoryHardCoded
import click


@click.group()
def cli_entry_point():
    pass


@cli_entry_point.command()
@click.argument('rdc_price')
def update_price(rdc_price):
    bdd = HotelRepositoryHardCoded()
    modify_hostel_room = ModifyHostelRoomPricesUseCase(hostel_room_bdd=bdd)
    modify_hostel_room.update_list_of_rooms(rdc_price=Price(float(rdc_price)))
    click.echo(f"Hostel room prices are now : {modify_hostel_room.hostel} -- IN MEMORY")


if __name__ == "__main__":
    cli_entry_point()
