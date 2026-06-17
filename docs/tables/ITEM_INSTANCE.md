# ITEM_INSTANCE

> Item Instance

**Description:** Item Instance desc  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQUISITION_COST` | DOUBLE |  |  | Acquisition Cost |
| 2 | `ACQUISITION_TYPE_CD` | DOUBLE |  |  | Acquisition Type |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `COMMISSION_DT_TM` | DATETIME |  |  | Commissioned Date/Time |
| 8 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Create Application Context |
| 9 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the Item Instance was created. |
| 10 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 11 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 12 | `CURRENT_LOCATION_CD` | DOUBLE |  |  | Current Location |
| 13 | `DISPOSAL_DT_TM` | DATETIME |  |  | Disposal Date/Time |
| 14 | `EXPIRE_DT_TM` | DATETIME |  |  | expire date and time value |
| 15 | `INSTANCE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 16 | `INSTANCE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of Item Instance (General, Equipment). |
| 17 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key |
| 18 | `LOAN_BORROW_IND` | DOUBLE |  |  | Loan / Borrow Indicator |
| 19 | `MANUFACTURER_CD` | DOUBLE |  |  | Manufacturer |
| 20 | `PERSON_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 21 | `PO_NBR` | VARCHAR(40) |  |  | Purchase Order Number |
| 22 | `PURCHASE_ORDER_ID` | DOUBLE |  |  | **OBSOLETE ** - Purchase Order primary key |
| 23 | `RENTAL_COST` | DOUBLE |  |  | Rental Cost |
| 24 | `RENTAL_USAGE_UOM_CD` | DOUBLE |  |  | Rental Usage Unit of Measure |
| 25 | `RENTED_DT_TM` | DATETIME |  |  | Rented Date/Time |
| 26 | `STATUS_CD` | DOUBLE |  |  | Status code value |
| 27 | `STERILE_IND` | DOUBLE |  |  | Sterile Indicator |
| 28 | `STORAGE_LOCATION_CD` | DOUBLE |  |  | Storage Location |
| 29 | `SVC_GROUP_CD` | DOUBLE |  |  | Service Group |
| 30 | `UNIQUE_FIELD` | VARCHAR(200) |  |  | Unique field which will hold the Serial Nbr and Mnemonic concatenated together for merging purposes. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 36 | `VENDOR_CD` | DOUBLE |  |  | Vendor associated with this account |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

