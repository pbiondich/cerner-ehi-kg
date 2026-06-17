# PRODUCT

> Stores demographic information about all blood bank products, whether a blood product or derivative. The main parent table in the PathNet Blood Bank Transfusion. Only common attributes about all products are stored in this table.

**Description:** Product  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_ID`  
**Columns:** 53  
**Referenced by:** 37 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALTERNATE_NBR` | VARCHAR(20) |  |  | This column can be used to record the original number labeled on the bag of blood, in the case of sites who choose to re-number blood products received from their supplier. This way they can still track the product by its original number, which is important in the for look-backs. |
| 6 | `BARCODE_NBR` | CHAR(20) |  |  | The original barcoded version of the product number, e.g., "1212345", which may have been translated into "G12345", depending on the alpha translation feature. |
| 7 | `BIOHAZARD_IND` | DOUBLE | NOT NULL |  | Indicates that the product is biohazardous. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `CORRECTED_IND` | DOUBLE |  |  | Indicates whether or not this product has been corrected in some way, such as its demographics changed, etc. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | Indicates the date and time the product row was created |
| 11 | `CUR_DISPENSE_DEVICE_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number. The primary key of the BB_DEVICE table. An identification of the device to which the product was dispensed. An example is "SURG FRIDGE #1", for a refrigerator within the surgical area. |
| 12 | `CUR_EXPIRE_DT_TM` | DATETIME |  |  | Defines when the product itself will expire. The current expiration date and time is entered at the time the product is received from the label on the product, but may be updated if it is modified or corrected. |
| 13 | `CUR_INV_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the current inventory area where the product resides. This inventory area is any area that keeps blood products or derivatives in an inventory, from which the products are dispensed. This means that the it could be the main blood bank, or a surgical area or emergency room that stocks blood for use in surgery. |
| 14 | `CUR_INV_DEVICE_ID` | DOUBLE | NOT NULL |  | Identifies the current inventory device where this product resides within inventory. An example would be "Freezer #1". This column is not currently used. |
| 15 | `CUR_INV_LOCN_CD` | DOUBLE | NOT NULL |  | The current location of this product as it relates to a patient's location. This column is only applicable when the product is actively dispensed or transfused to a patient. It is cleared out if the product is returned. |
| 16 | `CUR_OWNER_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the current blood bank owner area where the product resides. This owner area is a fully-functioning blood bank that is responsible for the blood received or drawn there. A blood bank owner area can have several inventory areas within it. An example of an owner area would be "General Hospital North", with its inventory areas being "Main BB - GH North", "Surgery - GH North", and "ER - GH North". |
| 17 | `CUR_SUPPLIER_ID` | DOUBLE | NOT NULL | FK→ | This column represents an organization_ID, which is the primary key to the ORGANIZATION table. It is an internal system-assigned number. It identifies the supplier of this product, the organization who sent the product to the transfusion service. |
| 18 | `CUR_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure in which this product's volume is recorded. It is entered at the time the product is received, from the label on the actual product (ex. "milliliters"). |
| 19 | `DISEASE_CD` | DOUBLE | NOT NULL |  | This column will store the unique identifier of the disease associated with the product. |
| 20 | `DONATED_BY_RELATIVE_IND` | DOUBLE |  |  | Obsolete. No longer used. - This column only applies to directed products received into the Blood Bank. It indicates whether or not the product was donated by a relative of the recipient or not. - This information is now on the AUTO_DIRECTED and CORRECTED_PRODUCT table. |
| 21 | `DONATION_TYPE_CD` | DOUBLE | NOT NULL |  | This column will store the unique identifier of the donation type associated. |
| 22 | `ELECTRONIC_ENTRY_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the primary product demographic fields were entered via Electronic Entry, and if so what form of entry was used. 0 - Product demographics are not guaranteed to have been entered electronically; 1 - Product demographics were scanned in via barcode reader |
| 23 | `FLAG_CHARS` | VARCHAR(2) |  |  | Stores the flag characters of an ISBT-128 donation number |
| 24 | `INTENDED_USE_PRINT_PARM_TXT` | VARCHAR(1) | NOT NULL |  | Contains the intended use of the product. It is derived from the ISBT ABORh Barcode. Valid values are:Autologous Crossover AAutologous Only 1 (one)Autologous Only Biohazard XDirected Biohazard 3Directed Only 2Directed Crossover DNot Specified 0 (zero)For Emergency Use Only !If the Product ABORH wasn't scanned in via ISBT Barcode, intended_use_print_parm_txt will be blank. |
| 25 | `INTERFACED_DEVICE_FLAG` | DOUBLE | NOT NULL |  | Indicates that the product is currently being tracked using an interfaced inventory tracking system. If it is set to be in a device, but the cur_dispense_device_id is 0, it means it is in transit. |
| 26 | `INTERFACE_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The product ID for a transferred product. |
| 27 | `LOCKED_IND` | DOUBLE |  |  | Indicates whether or not the product is locked for update by a particular blood bank transaction. Inquiry transactions do not update this indicator to locked. |
| 28 | `MODIFIED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This column represents the PRODUCT_ID of the original product from which this product was created through the product modification application. The product_id is the primary key of the PRODUCT table. It is an internal system-assigned number that uniquely identifies a product in the blood bank. |
| 29 | `MODIFIED_PRODUCT_IND` | DOUBLE |  |  | Indicates whether the product has been modified after it was received into the blood bank's inventory. This indicator is only updated on the "parent" product, not the new "child" products created from the original parent product. |
| 30 | `ORIG_INV_LOCN_CD` | DOUBLE | NOT NULL |  | The original location of this product in the blood bank's inventory at the time it was received. |
| 31 | `ORIG_SHIP_COND_CD` | DOUBLE | NOT NULL |  | The original condition in which the product was shipped to the transfusion service (ex. "Dry Ice"). |
| 32 | `ORIG_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure in which this product's volume was originally recorded. It is entered at the time the product is received, from the label on the actual product (ex. "milliliters"). |
| 33 | `ORIG_VIS_INSP_CD` | DOUBLE | NOT NULL |  | The outcome of the visual inspection when this product was received (ex. "OK", "Bag leaking", etc.). This visual inspection may cause the product to need to be quarantined. |
| 34 | `POOLED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This column represents the PRODUCT_ID of the new pooled product into which this product was pooled through the pooling application. The product_id is the primary key of the PRODUCT table. It is an internal system-assigned number that uniquely identifies a product in the blood bank. |
| 35 | `POOLED_PRODUCT_IND` | DOUBLE |  |  | Indicates whether the product is a pooled product, i.e.., a product that was created through the pooling process. This indicator is only updated on the newly created product, not the products that were components within the pool. |
| 36 | `POOL_OPTION_ID` | DOUBLE | NOT NULL |  | If this product was created by the pooling process, it identifies the pool option chosen by the user in the pooling transaction. |
| 37 | `PRODUCT_CAT_CD` | DOUBLE | NOT NULL |  | The category of products to which this specific type of product belongs. An example of a product category is "Plasma", which might include a product type of "Fresh Frozen Plasma", "Thawed Plasma", and "Salvaged Plasma". |
| 38 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The type of product (ex. "Fresh Frozen Plasma") derived from the label on the bag of blood. |
| 39 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL |  | The class of products to which this specific type of product belongs. Two classes of products may be used: blood products and derivatives. |
| 40 | `PRODUCT_ID` | DOUBLE | NOT NULL | PK | The primary key to this table. An internal system-assigned number that keeps each row unique. |
| 41 | `PRODUCT_NBR` | VARCHAR(20) | NOT NULL |  | The number assigned to this product to identify it. Also known as "unit number". It is entered at the time the product is received into the blood bank's inventory, from the label on the actual bag of blood. In the case of derivative products, it is the lot number from the batch of derivatives. |
| 42 | `PRODUCT_SUB_NBR` | CHAR(5) |  |  | A letter or number assigned to each product with the same product number, in order to make them unique. An example is splitting red blood cells into smaller bags of red cells. The sub number is assigned as "1", "2", "3", etc. or as "A", "B", "C", etc. |
| 43 | `PRODUCT_TYPE_BARCODE` | VARCHAR(22) |  |  | This is the barcode value that was etiered in BB Recieve Products or corrected in Correct Inventory. |
| 44 | `RECV_DT_TM` | DATETIME |  |  | The date and time the product was received into the blood bank's inventory from a supplier. This column is empty on products created from the pooling or modification process since they are not received but rather created by the blood bank. |
| 45 | `RECV_PRSNL_ID` | DOUBLE | NOT NULL |  | This column represents the person_id of the person from the personnel table (prsnl) that received this product into the blood bank's inventory. |
| 46 | `REQ_LABEL_VERIFY_IND` | DOUBLE | NOT NULL |  | Product requires label verify because a lebel was printed or mod opt was defined to print a label. |
| 47 | `SERIAL_NUMBER_TXT` | VARCHAR(22) |  |  | Contains GS1 serial number for derivative products when applicable |
| 48 | `STORAGE_TEMP_CD` | DOUBLE | NOT NULL |  | The temperature at which the product should be stored. |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CUR_SUPPLIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `INTERFACE_PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `MODIFIED_PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `POOLED_PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

## Referenced by (37)

| From table | Column |
|------------|--------|
| [ASSIGN](ASSIGN.md) | `PRODUCT_ID` |
| [ASSIGN_RELEASE](ASSIGN_RELEASE.md) | `PRODUCT_ID` |
| [AUTO_DIRECTED](AUTO_DIRECTED.md) | `PRODUCT_ID` |
| [BB_AUTODIR_EXCEPTION](BB_AUTODIR_EXCEPTION.md) | `PRODUCT_ID` |
| [BB_DEVICE_TRANSFER](BB_DEVICE_TRANSFER.md) | `PRODUCT_ID` |
| [BB_EDN_DSCRPNCY_OVRD](BB_EDN_DSCRPNCY_OVRD.md) | `PRODUCT_ID` |
| [BB_EXC_CXM_PRODUCT](BB_EXC_CXM_PRODUCT.md) | `PRODUCT_ID` |
| [BB_LABEL_VERIFY](BB_LABEL_VERIFY.md) | `PRODUCT_ID` |
| [BB_ORDER_CELL](BB_ORDER_CELL.md) | `PRODUCT_ID` |
| [BB_SHIP_EVENT](BB_SHIP_EVENT.md) | `PRODUCT_ID` |
| [BB_SPEC_EXP_OVRD_PROD](BB_SPEC_EXP_OVRD_PROD.md) | `PRODUCT_ID` |
| [BLOOD_PRODUCT](BLOOD_PRODUCT.md) | `PRODUCT_ID` |
| [CE_PRODUCT](CE_PRODUCT.md) | `PRODUCT_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `POOLED_PRODUCT_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `PRODUCT_ID` |
| [CROSSMATCH](CROSSMATCH.md) | `PRODUCT_ID` |
| [DERIVATIVE](DERIVATIVE.md) | `PRODUCT_ID` |
| [DESTRUCTION](DESTRUCTION.md) | `PRODUCT_ID` |
| [DISPENSE_RETURN](DISPENSE_RETURN.md) | `PRODUCT_ID` |
| [DISPOSITION](DISPOSITION.md) | `PRODUCT_ID` |
| [MODIFICATION](MODIFICATION.md) | `PRODUCT_ID` |
| [MODIFY_DEVICE](MODIFY_DEVICE.md) | `PRODUCT_ID` |
| [ORDERS](ORDERS.md) | `PRODUCT_ID` |
| [PATIENT_DISPENSE](PATIENT_DISPENSE.md) | `PRODUCT_ID` |
| [PRODUCT](PRODUCT.md) | `INTERFACE_PRODUCT_ID` |
| [PRODUCT](PRODUCT.md) | `MODIFIED_PRODUCT_ID` |
| [PRODUCT](PRODUCT.md) | `POOLED_PRODUCT_ID` |
| [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_ID` |
| [PRODUCT_NOTE](PRODUCT_NOTE.md) | `PRODUCT_ID` |
| [PRODUCT_RH_PHENOTYPE](PRODUCT_RH_PHENOTYPE.md) | `PRODUCT_ID` |
| [QUARANTINE](QUARANTINE.md) | `PRODUCT_ID` |
| [QUARANTINE_RELEASE](QUARANTINE_RELEASE.md) | `PRODUCT_ID` |
| [RECEIPT](RECEIPT.md) | `PRODUCT_ID` |
| [SPECIAL_TESTING](SPECIAL_TESTING.md) | `PRODUCT_ID` |
| [SPECIAL_TESTING_RESULT](SPECIAL_TESTING_RESULT.md) | `PRODUCT_ID` |
| [TRANSFER](TRANSFER.md) | `PRODUCT_ID` |
| [TRANSFUSION](TRANSFUSION.md) | `PRODUCT_ID` |

