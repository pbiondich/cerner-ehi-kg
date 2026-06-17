# OMF_PVI_FILTER

> PowerVision Filter information.

**Description:** PowerVision Filter information.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_NUM_ID` | DOUBLE |  |  | ID used in filtering - could be code_values, person_id's, encounter_id's, etc. |
| 2 | `BEG_PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | Parent entity name for beg_num_id. |
| 3 | `BEG_VALUE` | VARCHAR(255) |  |  | Beginning string value - when not using an ID. |
| 4 | `END_NUM_ID` | DOUBLE |  |  | ID used in filtering - could be code_values, person_id's, encounter_id's, etc. - end of range; not used now. |
| 5 | `END_PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | Parent entity name for end_num_id. |
| 6 | `END_VALUE` | VARCHAR(255) |  |  | Ending string value - when not using an ID. |
| 7 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Code value of the omf_indicator row that PowerVision is filtering on. Other codesets can be used besides 14265 depending on the team defining the value. |
| 8 | `OMF_PV_ITEM_ID` | DOUBLE | NOT NULL |  | Parent PowerVision Saved View or Filter. |
| 9 | `OPERAND` | VARCHAR(255) |  |  | Operand to use in filtering - e.g. != or = |
| 10 | `RVAL1` | VARCHAR(255) |  |  | Result value1 used for clinical event filtering. |
| 11 | `RVAL2` | VARCHAR(255) |  |  | Result value2 used for clinical event filtering. |
| 12 | `RVAL3` | VARCHAR(255) |  |  | Result value3 used for clinical event filtering. |
| 13 | `RVAL4` | VARCHAR(255) |  |  | Result value4 used for clinical event filtering. |
| 14 | `RVAL5` | VARCHAR(255) |  |  | Result value5 used for clinical event filtering. |
| 15 | `SRVAL1` | VARCHAR(255) |  |  | Sub result value1 used for microbiology filtering. |
| 16 | `SRVAL2` | VARCHAR(255) |  |  | Sub result value2 used for microbiology filtering. |
| 17 | `SRVAL3` | VARCHAR(255) |  |  | Sub result value3 used for microbiology filtering. |
| 18 | `SRVAL4` | VARCHAR(255) |  |  | Sub result value4 used for microbiology filtering. |
| 19 | `SRVAL5` | VARCHAR(255) |  |  | Sub result value5 used for microbiology filtering. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VAL1` | VARCHAR(255) |  |  | Generic filtering value - used by clinical event filtering currently. |
| 26 | `VAL2` | VARCHAR(255) |  |  | Generic filtering value - used by clinical event filtering currently. |
| 27 | `VAL3` | VARCHAR(255) |  |  | Generic filtering value - used by clinical event filtering currently. |
| 28 | `VAL4` | VARCHAR(255) |  |  | Generic filtering value - used by clinical event filtering currently. |
| 29 | `VAL5` | VARCHAR(255) |  |  | Generic filtering value - used by clinical event filtering currently. |
| 30 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Type of filter being stored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

