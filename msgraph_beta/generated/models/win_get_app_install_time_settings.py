from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WinGetAppInstallTimeSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties used to determine when to offer an app to devices and when to install the app on devices.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The time at which the app should be installed.
    deadline_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Whether the local device time or UTC time should be used when determining the deadline times.
    use_local_time: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WinGetAppInstallTimeSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppInstallTimeSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WinGetAppInstallTimeSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deadlineDateTime": lambda n : setattr(self, 'deadline_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "useLocalTime": lambda n : setattr(self, 'use_local_time', n.get_bool_value()),
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
        writer.write_datetime_value("deadlineDateTime", self.deadline_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("useLocalTime", self.use_local_time)
        writer.write_additional_data_value(self.additional_data)
    

