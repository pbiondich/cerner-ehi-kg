# CDI_AC_USER

> This table defines CPDI configurations for Ascent Capture users.

**Description:** CDI Ascent Capture User  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AC_USERNAME` | VARCHAR(32) | NOT NULL |  | The user name of the Ascent Capture user. |
| 2 | `AUDITING_IND` | DOUBLE | NOT NULL |  | Specifies whether or not to include this Ascent Capture user for auditing and reporting. |
| 3 | `CDI_AC_USER_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. |
| 4 | `MILL_USERNAME` | VARCHAR(50) |  |  | Millennium username that correlates to the kofax username. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization the Ascent Capture user is associated to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

