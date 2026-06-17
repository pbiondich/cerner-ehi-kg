# ACCRED_SYSTEM

> Stored information regarding the accred system.

**Description:** ACCREDITATION SYSTEM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCRED_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique ID associated with an accred system. The value for the ID will be re-generated nightly as the table contents are reloaded (replaced) |
| 2 | `ACCRED_SYSTEM_IDENT` | VARCHAR(250) | NOT NULL |  | Text identifier associated with an individual Accred_system_id |
| 3 | `INTERACTION_NAME` | VARCHAR(250) | NOT NULL |  | This value identifies the Interaction name associated with systemColumn |
| 4 | `INTERACTION_VERSION_TEXT` | VARCHAR(250) | NOT NULL |  | This value identifies the version of the Interaction name that the system supports |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It identifies the organization of the service. |
| 6 | `PARTY_KEY_TXT` | VARCHAR(250) | NOT NULL |  | Identifies a business service within an organization, which could be in the form of OCS-Instance, e.g., D81001-811. |
| 7 | `SERVICE_NAME` | VARCHAR(250) | NOT NULL |  | Identifies a business service within an organization, which could be in the form of OCS-Instance, e.g., D81001-811. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

