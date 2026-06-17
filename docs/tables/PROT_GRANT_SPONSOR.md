# PROT_GRANT_SPONSOR

> Stores information about institutions that sponsor the protocol in whole or in part.. For this purpose, an institution can be a research institute, drug company, government agency, etc.

**Description:** Stores information about institutions that sponsor the protocol  
**Table type:** REFERENCE  
**Primary key:** `PROT_GRANT_SPONSOR_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FUNDED_IND` | DOUBLE | NOT NULL |  | Indicator to specify if the organization supports the protocol with funds |
| 2 | `GRANT_NBR` | VARCHAR(255) |  |  | The grant number for the organization's support |
| 3 | `GRANT_PROJECT_TITLE` | VARCHAR(255) |  |  | This field contains a description of the grant/grant project that is supporting the protocol. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely idenitifies a row in the organization table. This field identifies an institution that is sponsoring the protocol in whole or in part.. For this purpose, an institution can be a research institute, drug company, government agency, etc. |
| 5 | `PRIMARY_SECONDARY_CD` | DOUBLE | NOT NULL |  | This field contains a code indicating whether this grant is the primary source of support for the protocol or a secondary source of support for the protocol. |
| 6 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the amendment |
| 7 | `PROT_GRANT_SPONSOR_ID` | DOUBLE | NOT NULL | PK | Primary Key |
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
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SUPPORT_TYPE](SUPPORT_TYPE.md) | `PROT_GRANT_SPONSOR_ID` |

