# MFA_IDENTITY_TYPE

> Stores information about the defined Identity Types, and the Method implementations which are configured to support them.

**Description:** MFA Identity Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS_NAME` | VARCHAR(260) |  |  | FQN of the Java class which supports this identity type |
| 2 | `IDENTITY_TYPE_NAME` | VARCHAR(45) | NOT NULL |  | UNIQUE NAME FOR AN IDENTITY TYPE |
| 3 | `IDENTITY_TYPE_VAL` | DOUBLE | NOT NULL |  | A Unique Value (Enumeration) created by the application which identifies an Identity Type. |
| 4 | `LIBRARY_NAME` | VARCHAR(260) |  |  | Name of the DLL which supports this identity type |
| 5 | `MFA_IDENTITY_TYPE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `MFA_METHOD_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the METHOD table |
| 7 | `TIMEOUT_AMT` | DOUBLE |  |  | Amount of time framework will allow for Method to perform its authentication before cancelling the attempt and continuing. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MFA_METHOD_ID` | [MFA_METHOD](MFA_METHOD.md) | `MFA_METHOD_ID` |

