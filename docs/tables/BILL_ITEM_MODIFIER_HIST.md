# BILL_ITEM_MODIFIER_HIST

> Stores all the Charge service Pricing, Bill Item related modifications and for tracking the History of changes.

**Description:** Bill Item Modifier History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 53

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID of the bill item on the bill_item table to which this modification is associated. This is the unique primary identifier of the bill_item table. |
| 7 | `BILL_ITEM_MODIFIER_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BILL_ITEM_MODIFIER_HIST table. |
| 8 | `BILL_ITEM_MOD_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the bill item modifier table. It is an internal system assigned number. |
| 9 | `BILL_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | Code from 13019 that indicates what type of bill item modifier this row is, such as addon, bill code, or charge point. |
| 10 | `BIM1_IND` | DOUBLE |  |  | This field holds the indicator for result as quantity for workload. |
| 11 | `BIM1_INT` | DOUBLE |  |  | To persist priority, quantity or Order based on the bill code type as per the original table. |
| 12 | `BIM1_NBR` | DOUBLE |  |  | This field holds the unit override for workload. This will allow the user to override the units default off of the workload_code table and enter a different value. To persist QCF, workload units as per the original table |
| 13 | `BIM2_INT` | DOUBLE |  |  | This field stores a multiplier based on the type code. To persist multiplier override as per the original table. |
| 14 | `BIM_IND` | DOUBLE |  |  | This field stores the projected indicator based on the type cd. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `KEY1` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 17 | `KEY10` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 18 | `KEY11` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 19 | `KEY11_ID` | DOUBLE | NOT NULL |  | Reserved for future use as per the original table. |
| 20 | `KEY12` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 21 | `KEY12_ID` | DOUBLE | NOT NULL |  | For Workload only, contains the code value of the template to be used for interval calculation of Workload units. This is an optional value. Still considering whether this value can be specified here or if it must come from the Workload Standard. To persist the possible values as per the modifications on the bill items.template_cd (14274), CODE_ VALUE parent entity. |
| 22 | `KEY13` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 23 | `KEY13_ID` | DOUBLE | NOT NULL |  | Indicates whether this workload row should be considered projected or not. This is used primarily by Work Assignment in pulling projected workload values into the application. |
| 24 | `KEY14` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 25 | `KEY14_ID` | DOUBLE | NOT NULL |  | To persist the possible values as per the modifications on the bill items.workload_standard_id, WORKLOAD_STANDARD parent entity |
| 26 | `KEY15` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 27 | `KEY15_ID` | DOUBLE | NOT NULL |  | Unique identifier to the code_value table for the item for count on the workload. This is usually going to be a (-1) to indicate that the value on the standard is not being overridden. To persist the possible values as per the modifications on the bill items.item_for_count_cd(15229), CODE_ VALUE parent entity. |
| 28 | `KEY1_ENTITY_NAME` | VARCHAR(30) |  |  | To persist the Key1 Entity Name which is usually 'CODE_VALUE' as per the original table Bill_Item_Modifier. |
| 29 | `KEY1_ID` | DOUBLE | NOT NULL |  | To persist the possible values as per the modifications on the bill items.14002 (code schedules,charge point schedules,code schedules),value from 305570 (stores prompts),bill item id of the addon |
| 30 | `KEY2` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 31 | `KEY2_ENTITY_NAME` | VARCHAR(30) |  |  | To persist the Key2 Entity Name which is usually 'CODE_VALUE' as per the original table Bill_Item_Modifier. |
| 32 | `KEY2_ID` | DOUBLE | NOT NULL |  | Depending on the bill_item_type_cd, this is the priority of bill codes; for charge points it is the code value from 13029 for the actual charge point; and for addons, is the code value from 106 (external owner). |
| 33 | `KEY3` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 34 | `KEY3_ENTITY_NAME` | VARCHAR(30) |  |  | To persist the Key3 Entity Name which is usually 'CODE_VALUE' as per the original table Bill_Item_Modifier. |
| 35 | `KEY3_ID` | DOUBLE | NOT NULL |  | To persist the possible values as per the modifications on the bill items.workload_code_id, nomen_id |
| 36 | `KEY4` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 37 | `KEY4_ENTITY_NAME` | VARCHAR(30) |  |  | To persist the Key4 Entity Name which is usually 'CODE_VALUE' as per the original table Bill_Item_Modifier. |
| 38 | `KEY4_ID` | DOUBLE | NOT NULL |  | To persist the possible values as per the modifications on the bill items.charge level from 13020 |
| 39 | `KEY5` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 40 | `KEY5_ENTITY_NAME` | VARCHAR(30) |  |  | To persist the Key5 Entity Name which is usually 'CODE_VALUE' as per the original table Bill_Item_Modifier. |
| 41 | `KEY5_ID` | DOUBLE | NOT NULL |  | To persist the possible values as per the modifications on the bill items.code value forrevenue codes(20769) and modifiers (17769) |
| 42 | `KEY6` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. (Bill codes). |
| 43 | `KEY7` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. (Description) |
| 44 | `KEY8` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 45 | `KEY9` | VARCHAR(200) |  |  | To persist Key information associated to a bill item except the prices. |
| 46 | `MODIFICATION_DT_TM` | DATETIME | NOT NULL |  | Represents the modified date and time of the parent record. |
| 47 | `PERMANENT_DEL_IND` | DOUBLE | NOT NULL |  | The indicator to mark History records that are no longer needed and are made eligible for permanent deletion. |
| 48 | `TASK_ACTION_FLAG` | DOUBLE | NOT NULL |  | To persist and represent the type of Task action performed/ or the correspodning history row represents.(Values 0= Add, 1= Update, 2= Delete) |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `BILL_ITEM_MOD_ID` | [BILL_ITEM_MODIFIER](BILL_ITEM_MODIFIER.md) | `BILL_ITEM_MOD_ID` |

