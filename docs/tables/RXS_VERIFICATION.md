# RXS_VERIFICATION

> Stores verification events performed on RxStation entities

**Description:** RxStation Verification  
**Table type:** ACTIVITY  
**Primary key:** `RXS_VERIFICATION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was created. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier that refers to the entity that is verified |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the entity that is verified |
| 4 | `RXS_VERIFICATION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rxs_verification table. |
| 5 | `STATUS_CD` | DOUBLE | NOT NULL |  | Verification status (e.g. success, failure, etc.) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VERIFICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Verification type code (e.g. barcode scanning, authentication, etc.) |
| 12 | `VERIFIED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier that refers to the person that performs the verification |
| 13 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | Workflow in which the verification is performed |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VERIFIED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RXS_VERIFICATION_ATTR](RXS_VERIFICATION_ATTR.md) | `RXS_VERIFICATION_ID` |

