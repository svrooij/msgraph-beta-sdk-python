from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.windows_updates.updatable_asset import UpdatableAsset

@dataclass
class UpdateAudiencePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The addExclusions property
    add_exclusions: Optional[list[UpdatableAsset]] = None
    # The addMembers property
    add_members: Optional[list[UpdatableAsset]] = None
    # The removeExclusions property
    remove_exclusions: Optional[list[UpdatableAsset]] = None
    # The removeMembers property
    remove_members: Optional[list[UpdatableAsset]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateAudiencePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAudiencePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateAudiencePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.windows_updates.updatable_asset import UpdatableAsset

        from .......models.windows_updates.updatable_asset import UpdatableAsset

        fields: dict[str, Callable[[Any], None]] = {
            "addExclusions": lambda n : setattr(self, 'add_exclusions', n.get_collection_of_object_values(UpdatableAsset)),
            "addMembers": lambda n : setattr(self, 'add_members', n.get_collection_of_object_values(UpdatableAsset)),
            "removeExclusions": lambda n : setattr(self, 'remove_exclusions', n.get_collection_of_object_values(UpdatableAsset)),
            "removeMembers": lambda n : setattr(self, 'remove_members', n.get_collection_of_object_values(UpdatableAsset)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("addExclusions", self.add_exclusions)
        writer.write_collection_of_object_values("addMembers", self.add_members)
        writer.write_collection_of_object_values("removeExclusions", self.remove_exclusions)
        writer.write_collection_of_object_values("removeMembers", self.remove_members)
        writer.write_additional_data_value(self.additional_data)
    

