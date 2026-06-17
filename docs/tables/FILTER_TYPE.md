# FILTER_TYPE

> This table contains the filter types defined to be used for the filter entity relation.

**Description:** Filter Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOW_EXCLUSION_IND` | DOUBLE |  |  | Allow exclusion indicator |
| 2 | `BUILD_TOOL_IND` | DOUBLE |  |  | build tool indicator |
| 3 | `FILTER_ENTITY1_NAME` | VARCHAR(30) | NOT NULL |  | filter entity1 name |
| 4 | `FILTER_ENTITY2_NAME` | VARCHAR(30) |  |  | filter entity2 name |
| 5 | `FILTER_ENTITY3_NAME` | VARCHAR(30) |  |  | filter entity3 name |
| 6 | `FILTER_ENTITY4_NAME` | VARCHAR(30) |  |  | filter entity4 name |
| 7 | `FILTER_ENTITY5_NAME` | VARCHAR(30) |  |  | filter entity5 name |
| 8 | `FILTER_TYPE1_ID` | DOUBLE | NOT NULL |  | FILTER TYPE1 IDENTIFIER |
| 9 | `FILTER_TYPE1_TXT` | VARCHAR(12) | NOT NULL |  | FILTER TYPE1 TEXT |
| 10 | `FILTER_TYPE2_ID` | DOUBLE | NOT NULL |  | FILTER TYPE2 IDENTIFIER |
| 11 | `FILTER_TYPE2_TXT` | VARCHAR(12) |  |  | FILTER TYPE2 TEXT |
| 12 | `FILTER_TYPE3_ID` | DOUBLE | NOT NULL |  | FILTER TYPE3 IDENTIFIER |
| 13 | `FILTER_TYPE3_TXT` | VARCHAR(12) |  |  | FILTER TYPE3 TEXT |
| 14 | `FILTER_TYPE4_ID` | DOUBLE | NOT NULL |  | FILTER TYPE4 IDENTIFIER |
| 15 | `FILTER_TYPE4_TXT` | VARCHAR(12) |  |  | FILTER TYPE4 TEXT |
| 16 | `FILTER_TYPE5_ID` | DOUBLE | NOT NULL |  | FILTER TYPE5 IDENTIFIER |
| 17 | `FILTER_TYPE5_TXT` | VARCHAR(12) |  |  | FILTER TYPE5 TEXT |
| 18 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL | FK→ | FILTER TYPE CODE |
| 19 | `GET_SCRIPT_NAME` | VARCHAR(32) | NOT NULL |  | get script name |
| 20 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 21 | `PARENT_TYPE_ID` | DOUBLE | NOT NULL |  | parent type identifier |
| 22 | `PARENT_TYPE_TXT` | VARCHAR(12) | NOT NULL |  | parent type text |
| 23 | `SEARCH_COMPONENT_NAME` | VARCHAR(32) | NOT NULL |  | search component name |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

