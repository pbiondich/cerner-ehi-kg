# HPD_PROVIDER

> Stores the networked provider information

**Description:** Healthcare Provider Directory Provider  
**Table type:** REFERENCE  
**Primary key:** `HPD_PROVIDER_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DATE_OF_BIRTH` | VARCHAR(15) |  |  | Provider's Date of Birth - used to help uniquely identify a provider. |
| 3 | `FIRST_NAME` | VARCHAR(100) | NOT NULL |  | First Name of the Provider |
| 4 | `GENDER_CD` | DOUBLE | NOT NULL |  | Gender of the Provider |
| 5 | `HPD_PROVIDER_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 6 | `INTERNAL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Provider corresponding to an internally defined personnel from the PRSNL table |
| 7 | `LAST_NAME` | VARCHAR(100) | NOT NULL |  | Last Name of the Provider |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `MIDDLE_NAME` | VARCHAR(100) |  |  | Middle Name of the Provider |
| 10 | `PREFIX_TXT` | VARCHAR(100) |  |  | Title prepended to the provider's name |
| 11 | `PROVIDER_NPI` | VARCHAR(20) |  |  | National Provider Identifier (NPI) is a Health Insurance Portability and Accountability Act (HIPAA) Administrative Simplification Standard. The NPI is a unique identification number for covered health care providers. |
| 12 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Current revision of the table. This should be incremented 1 higher than the highest revision on the table. All rows in the same update should have the same revision. |
| 13 | `SUFFIX_TXT` | VARCHAR(100) |  |  | Title appended to the provider's name |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERNAL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HPD_MEMBERSHIP](HPD_MEMBERSHIP.md) | `HPD_PROVIDER_ID` |

