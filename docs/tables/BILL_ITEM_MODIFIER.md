# BILL_ITEM_MODIFIER

> Additional information connected to a bill item that may modify pricing of bill items such as addon items, charge points, bill codes. Bill_item_type_cd defines the type of modification.

**Description:** Bill Item Modifier  
**Table type:** REFERENCE  
**Primary key:** `BILL_ITEM_MOD_ID`  
**Columns:** 49  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID of the bill item on the bill_item table to which this modification is associated. This is the unique primary identifier of the bill_item table. |
| 7 | `BILL_ITEM_MOD_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the bill item modifier table. It is an internal system assigned number. |
| 8 | `BILL_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | Code from 13019 that indicates what type of bill item modifier this row is, such as addon, bill code, or charge point. |
| 9 | `BIM1_IND` | DOUBLE |  |  | This field holds the indicator for result as quantity for workload. |
| 10 | `BIM1_INT` | DOUBLE |  |  | This field stores the quantity, priority or binary representation based on the type cd. |
| 11 | `BIM1_NBR` | DOUBLE |  |  | This field holds the unit override for workload. This will allow the user to override the units default off of the workload_code table and enter a different value. |
| 12 | `BIM2_INT` | DOUBLE |  |  | This field stores a multiplier based on the type code. |
| 13 | `BIM_IND` | DOUBLE |  |  | This field stores the projected indicator based on the type cd. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `KEY1` | VARCHAR(200) |  |  | not used |
| 16 | `KEY10` | VARCHAR(200) |  |  | not used |
| 17 | `KEY11` | VARCHAR(200) |  |  | not used |
| 18 | `KEY11_ID` | DOUBLE | NOT NULL |  | For Workload only, contains an override value for the multiplier, or (-1) if there is no override. |
| 19 | `KEY12` | VARCHAR(200) |  |  | not used |
| 20 | `KEY12_ID` | DOUBLE | NOT NULL |  | For Workload only, contains the code value of the template to be used for interval calculation of Workload units. This is an optional value. Still considering whether this value can be specified here or if it must come from the Workload Standard. |
| 21 | `KEY13` | VARCHAR(200) |  |  | not used |
| 22 | `KEY13_ID` | DOUBLE | NOT NULL |  | Indicates whether this workload row should be considered projected or not. This is used primarily by Work Assignment in pulling projected workload values into the application. |
| 23 | `KEY14` | VARCHAR(200) |  |  | not used |
| 24 | `KEY14_ID` | DOUBLE | NOT NULL |  | The unique identifier to the workload_standard table. |
| 25 | `KEY15` | VARCHAR(200) |  |  | not used |
| 26 | `KEY15_ID` | DOUBLE | NOT NULL |  | Unique identifier to the code_value table for the item for count on the workload. This is usually going to be a (-1) to indicate that the value on the standard is not being overridden. |
| 27 | `KEY1_ENTITY_NAME` | VARCHAR(32) |  |  | not used |
| 28 | `KEY1_ID` | DOUBLE | NOT NULL |  | Depending on the bill_item_type_cd, this is the code value of the charge point or bill code schedule from 14002, or it is the bill_item_id of the addon from the bill_item table. |
| 29 | `KEY2` | VARCHAR(200) |  |  | not used |
| 30 | `KEY2_ENTITY_NAME` | VARCHAR(32) |  |  | not used |
| 31 | `KEY2_ID` | DOUBLE | NOT NULL |  | Depending on the bill_item_type_cd, this is the priority of bill codes; for charge points it is the code value from 13029 for the actual charge point; and for addons, is the code value from 106 (external owner). |
| 32 | `KEY3` | VARCHAR(200) |  |  | not used |
| 33 | `KEY3_ENTITY_NAME` | VARCHAR(32) |  |  | not used |
| 34 | `KEY3_ID` | DOUBLE | NOT NULL |  | Depending on the bill_item_type_cd, this is not used for bill codes; it indicates whether the charge point is manual for charge points; and represents the quantity of the addon. |
| 35 | `KEY4` | VARCHAR(200) |  |  | not used |
| 36 | `KEY4_ENTITY_NAME` | VARCHAR(32) |  |  | not used |
| 37 | `KEY4_ID` | DOUBLE | NOT NULL |  | not used |
| 38 | `KEY5` | VARCHAR(200) |  |  | not used |
| 39 | `KEY5_ENTITY_NAME` | VARCHAR(32) |  |  | not used |
| 40 | `KEY5_ID` | DOUBLE | NOT NULL |  | not used |
| 41 | `KEY6` | VARCHAR(200) |  |  | Depending on the bill_item_type_cd, this is the bill code; not used for charge points; is the description of the addon. |
| 42 | `KEY7` | VARCHAR(350) |  |  | Depending on the bill_item_type_cd, it is the description of the bill code; not used for charge points; not used for addons. |
| 43 | `KEY8` | VARCHAR(200) |  |  | not used |
| 44 | `KEY9` | VARCHAR(200) |  |  | not used |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BCE_EVENT_BILL_MOD_RELTN](BCE_EVENT_BILL_MOD_RELTN.md) | `BILL_ITEM_MOD_ID` |
| [BILL_ITEM_MODIFIER_HIST](BILL_ITEM_MODIFIER_HIST.md) | `BILL_ITEM_MOD_ID` |
| [PFT_FEE_SCHED_RELTN](PFT_FEE_SCHED_RELTN.md) | `BILL_ITEM_MOD_ID` |

