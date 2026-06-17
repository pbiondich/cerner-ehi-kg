# BR_AUTO_RLI_ORDER

> Contains the orderable items for a reference lab. This is a Bedrock autobuild content table used in the reference lab order wizard.

**Description:** Bedrock Auto RLI order  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CLASS` | VARCHAR(100) |  |  | Description of the accession class for the orderable item. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ALIAS_NAME` | VARCHAR(100) |  |  | Alias value for the orderable item, supplied by the reference lab. |
| 4 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 5 | `COLLECTION_CLASS` | VARCHAR(100) |  |  | Description of the collection class for the orderable item. |
| 6 | `COLLECTION_METHOD` | VARCHAR(100) |  |  | Description of the collection method for the orderable item. |
| 7 | `CONCEPT_CKI` | VARCHAR(100) |  |  | stores the Cerner-assigned concept_cki value that is assigned to the orderable item |
| 8 | `CONTAINER` | VARCHAR(300) |  |  | Description of the container for the orderable item. |
| 9 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | Indicator value defining whether the orderable item is automatically selected. |
| 10 | `DEPT_NAME` | VARCHAR(100) |  |  | Department name for the orderable item. |
| 11 | `MIN_VOL` | DOUBLE |  |  | Minimum volume required for the orderable item specimen. |
| 12 | `MIN_VOL_UNITS` | VARCHAR(100) |  |  | Description of the minimum volume units for the orderable item. |
| 13 | `MIN_VOL_VALUE` | DOUBLE |  |  | value of the minimum volume |
| 14 | `ORDER_DESC` | VARCHAR(100) |  |  | Long description of the orderable item. |
| 15 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | Mnemonic of the orderable item. |
| 16 | `PARENT_ORDER_ID` | DOUBLE |  |  | stores the id of the primary parent row on the br_auto_rli_table, and signifies that this is a child row |
| 17 | `PERFORMING_LOC` | VARCHAR(100) |  |  | String defining where the order is performed. |
| 18 | `RLI_ORDER_ID` | DOUBLE | NOT NULL |  | Unique identifier for the reference lab orderable item. |
| 19 | `SPECIAL_HANDLING` | VARCHAR(100) |  |  | Description of the special handling instructions for the orderable item. |
| 20 | `SPECIMEN_TYPE` | VARCHAR(100) |  |  | Description of the specimen type for the orderable item. |
| 21 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Flag value identifying the reference lab. |
| 22 | `SUPPLIER_MNEMONIC` | VARCHAR(100) |  |  | Reference lab's mnemonic for the orderable item. |
| 23 | `TRANSFER_TEMP` | VARCHAR(100) |  |  | Description of the transfer temperature for the orderable item. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

