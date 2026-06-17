# RULE_DEFINITION

> Rule Definition

**Description:** Rule Definition  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 2 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code set. |
| 3 | `MERGE_ID` | DOUBLE | NOT NULL |  | Code set or id |
| 4 | `MERGE_NAME` | VARCHAR(250) | NOT NULL |  | Merge_name & Merge_id are used only for values that come from code_values or other tables. |
| 5 | `PARAM_NAME` | VARCHAR(250) | NOT NULL |  | Nameof the parameter type. |
| 6 | `PARAM_VALUE` | VARCHAR(250) | NOT NULL |  | Parameter value.e.g.:If the Param Name is 'Age of Request', the parameter value could be 1. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | It would be the Expire_Rule_Id in Expire_Rule table. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | It would be "Expire_Rule" table name. |
| 9 | `RULE_DEFINITION_ID` | DOUBLE | NOT NULL |  | Primary key of Rule_Definition table. |
| 10 | `RULE_TYPE_CD` | DOUBLE | NOT NULL |  | Rule Type Code |
| 11 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Sequence Number |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

