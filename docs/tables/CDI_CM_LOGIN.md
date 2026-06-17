# CDI_CM_LOGIN

> This table defines users that can be used to login to the 3rd party content management system.

**Description:** CDI Content Management Login  
**Table type:** REFERENCE  
**Primary key:** `CDI_CM_LOGIN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_CM_LOGIN_ID` | DOUBLE | NOT NULL | PK | The unique primary key for this table. |
| 2 | `CM_PASSWORD` | VARCHAR(64) | NOT NULL |  | The password for the 3rd party system. |
| 3 | `CM_USERNAME` | VARCHAR(64) | NOT NULL |  | The username for the 3rd party system. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization the user is associated with. |
| 5 | `ORG_DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that this is the default user to be used for any position that does not have a specific user associated. |
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

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_CM_LOGIN_POSITION](CDI_CM_LOGIN_POSITION.md) | `CDI_CM_LOGIN_ID` |

