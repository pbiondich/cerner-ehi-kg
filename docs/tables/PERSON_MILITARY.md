# PERSON_MILITARY

> The person military table contains various attributes about a person that is a member of the military.

**Description:** Person Military  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSIGNED_UNIT_ORG_ID` | DOUBLE | NOT NULL | FK→ | The military unit organization to which the military person's placement is relatively permanent. This is the value of the unique primary identifier of the organization table. it is an internal system assigned number. |
| 6 | `ATTACHED_UNIT_ORG_ID` | DOUBLE | NOT NULL | FK→ | The military unit organization to which the military person's placement is relatively temporary.This is the value of the unique primary identifier of the organization table. it is an internal system assigned number. |
| 7 | `COMMAND_SECURITY_CD` | DOUBLE | NOT NULL |  | Represents the special access security program for the military person's command. It informs the user of the service member¿s responsibilities and can impact the care and medications that can be given to the patient. The special access programs require additional security protection, safeguards, and access restrictions which exceed those for regular classified information. |
| 8 | `FLYING_STATUS_CD` | DOUBLE | NOT NULL |  | Represents if the person is authorized and qualified (both technically and medically) for flight. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_UNIT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ATTACHED_UNIT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

