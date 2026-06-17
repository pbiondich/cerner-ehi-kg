# CT_USER_DOMAIN_INFO

> This table stores the user sign on information for each Discovere domain.

**Description:** User sign on information for each Discovere domain.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CT_DOMAIN_INFO_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ct_domain_info table. |
| 2 | `CT_USER_DOMAIN_INFO_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `USER_TOKEN_TXT` | VARCHAR(255) | NOT NULL |  | This field contains the user's token sign on information string. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_DOMAIN_INFO_ID` | [CT_DOMAIN_INFO](CT_DOMAIN_INFO.md) | `CT_DOMAIN_INFO_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

