# PHA_FLEX

> The PHA_FLEX table stores the relationships of various flexed entities by location (ie Facility, Nurse Unit, etc.).

**Description:** PHA_FLEX  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL | FK→ | How the reference entity is further flexed to the financial class of the patient. |
| 8 | `FLEX_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies how ref_entity_id is flexed. (i.e. Facility, Nurse Unit, etc.) |
| 9 | `FLEX_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Flex_entity_id filename. |
| 10 | `FUNDING_SOURCE_CD` | DOUBLE | NOT NULL |  | Describes the entity providing funding to purchase a pharmaceutical product. |
| 11 | `NEW_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies new code value or field id that is the result of flexing the ref_entity_id by the flex field identified in flex_entity_id. |
| 12 | `NEW_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | New_entity_id filename. |
| 13 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy Type Cd |
| 14 | `PHA_FLEX_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pha_flex table. It is an internal system assigned number. |
| 15 | `REF_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies reference code value or field id that will be changed. |
| 16 | `REF_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Ref_entity_id filename. |
| 17 | `SUB_FLEX_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies how the REFERENCE ENTITY is further flexed, i.e., ENCOUNTER_TYPE_CD. |
| 18 | `SUB_FLEX_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies how the REFERENCE ENTITY is further flexed, i.e., ENCOUNTER_TYPE_CD. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FINANCIAL_CLASS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

