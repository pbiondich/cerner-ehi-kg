# MED_DEF_FLEX

> The Med_def_flex file stores the various methods of flexing a Med_def, including Pharmacy type, Location (Facility, Nursing Unit, Ambulatory, Pharmacy), Package Type. These records are 1 to many to the Med_def.

**Description:** Med_Def_Flex  
**Table type:** REFERENCE  
**Primary key:** `MED_DEF_FLEX_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FLEX_SORT_FLAG` | DOUBLE |  |  | Flex Sort Flag |
| 6 | `FLEX_TYPE_CD` | DOUBLE | NOT NULL |  | flex_type_cd |
| 7 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item_id |
| 8 | `MED_DEF_FLEX_ID` | DOUBLE | NOT NULL | PK | med_def_flex_id |
| 9 | `MED_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | med package type id |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | parent entity id |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Parent entity name |
| 12 | `PARENT_MED_DEF_FLEX_ID` | DOUBLE | NOT NULL | FK→ | parent med def flex id |
| 13 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | pharmacy type cd |
| 14 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `MED_PACKAGE_TYPE_ID` | [MED_PACKAGE_TYPE](MED_PACKAGE_TYPE.md) | `MED_PACKAGE_TYPE_ID` |
| `PARENT_MED_DEF_FLEX_ID` | [MED_DEF_FLEX](MED_DEF_FLEX.md) | `MED_DEF_FLEX_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MED_DEF_FLEX](MED_DEF_FLEX.md) | `PARENT_MED_DEF_FLEX_ID` |
| [MED_FLEX_OBJECT_IDX](MED_FLEX_OBJECT_IDX.md) | `MED_DEF_FLEX_ID` |
| [MED_IDENTIFIER](MED_IDENTIFIER.md) | `MED_DEF_FLEX_ID` |

