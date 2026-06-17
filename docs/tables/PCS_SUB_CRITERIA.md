# PCS_SUB_CRITERIA

> Stores the sub criteria used for Clinical Validation. This table will be used primarily for microbiology clinical validation information.

**Description:** Stores the sub criteria used for Clinical Validation  
**Table type:** REFERENCE  
**Primary key:** `SUB_CRITERIA_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pcs_criteria table. |
| 7 | `CRITERIA_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of the criteria type. Code set 29161 |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `MAX_VALUE` | DOUBLE | NOT NULL |  | Maximum value of a range type criteria, which is used when the selected Susceptibility Detail is a numeric type. |
| 10 | `MICRO_TASK_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for certain type of microbiology criteria (ex: reports, and response). Code set 14929. |
| 11 | `MIN_VALUE` | DOUBLE | NOT NULL |  | Minimum value of a range type criteria, which is used when the selected Susceptibility Detail is a numeric type. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | id number of the selected criteria located on table . |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table name where selected criteria is stored. Valid names include:CODE_VALUE, PRSNL, ORDER_CATALOG, LOCATION, SERVICE_RESOURCE, MIC_GROUP_RESPONSE |
| 14 | `SUB_CRITERIA_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the sub criteria |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITERIA_ID` | [PCS_CRITERIA](PCS_CRITERIA.md) | `CRITERIA_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_QUALIFYING_CRITERIA](PCS_QUALIFYING_CRITERIA.md) | `SUB_CRITERIA_ID` |

