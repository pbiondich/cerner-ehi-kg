# IND_IDE_OWNERSHIP

> This table stores ownership information on investigational new drug or device

**Description:** INVESTIGATIONAL NEW DRUG INVESTIGATIONAL DEVICE OWNERSHIP  
**Table type:** REFERENCE  
**Primary key:** `IND_IDE_OWNERSHIP_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT_DEV_ID` | DOUBLE | NOT NULL |  | This field identifies the investigational new drug or device whose ownership is being recorded. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `IND_IDE_NBR` | VARCHAR(6) |  |  | The number of the IND/IDE |
| 5 | `IND_IDE_OWNERSHIP_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 6 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization which owns the drug/device |
| 7 | `OWNERSHIP_ID` | DOUBLE | NOT NULL | FK→ | A unique key for the Investigation Drug or Device's Owner on a protocol. No two active rows can have the same ownership_id. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | The role which owns the drug/device |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | The date from which IND/IDE is valid |
| 16 | `VALID_TO_DT_TM` | DATETIME | NOT NULL |  | The date till which IND/IDE is valid |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OWNERSHIP_ID` | [IND_IDE_OWNERSHIP](IND_IDE_OWNERSHIP.md) | `IND_IDE_OWNERSHIP_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [IND_IDE_OWNERSHIP](IND_IDE_OWNERSHIP.md) | `OWNERSHIP_ID` |

