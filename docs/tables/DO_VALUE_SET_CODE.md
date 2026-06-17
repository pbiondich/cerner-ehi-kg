# DO_VALUE_SET_CODE

> Defines a code/identifier within a value set.

**Description:** Discern Ontology Value Set Code  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_IDENTIFIER` | VARCHAR(512) | NOT NULL |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies an Cerner or industry idenfier for a code within a value set.; Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies a single row in the VOCABULARIES or CODE_SYSTEMS table. |
| 2 | `DO_NAMESPACE` | VARCHAR(128) | NOT NULL |  | Based on the type of the mapping i.e. Proprietary to Standard or Standard to Proprietary Or Proprietary to Proprietary, this uniquely identifies a well known identifier for the valueset (ex. FHIR code representing the set). |
| 3 | `DO_VALUE_SET_CODE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_VALUE_SET_CODE table. |
| 4 | `DO_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | The Value Set Identifier, a row in the DO_SCOPE database table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_VALUE_SET_ID` | [DO_VALUE_SET](DO_VALUE_SET.md) | `DO_VALUE_SET_ID` |

