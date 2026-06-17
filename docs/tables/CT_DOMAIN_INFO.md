# CT_DOMAIN_INFO

> This table stores the Discovere domain information

**Description:** Discovere Domain Information  
**Table type:** REFERENCE  
**Primary key:** `CT_DOMAIN_INFO_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CT_DOMAIN_INFO_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 3 | `DOMAIN_NAME` | VARCHAR(255) | NOT NULL |  | This field contains the name of the domain. |
| 4 | `DOMAIN_NAME_IDENT` | VARCHAR(255) | NOT NULL |  | Key for domain. Contains the Domain Name key data. uniquely identifies an active row of data. This name will be entered via front end tool and will be unique for active/effective rows. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `PREV_CT_DOMAIN_INFO_ID` | DOUBLE | NOT NULL | FK→ | The original value of the ct_domain_info_id used for grouping the related versons. Required for type 2 versioning methodology. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `URL1_TXT` | VARCHAR(255) | NOT NULL |  | This field contains the first domain URL string. |
| 14 | `URL2_TXT` | VARCHAR(255) | NOT NULL |  | This field contains the second domain URL string. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PREV_CT_DOMAIN_INFO_ID` | [CT_DOMAIN_INFO](CT_DOMAIN_INFO.md) | `CT_DOMAIN_INFO_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CT_DOMAIN_INFO](CT_DOMAIN_INFO.md) | `PREV_CT_DOMAIN_INFO_ID` |
| [CT_USER_DOMAIN_INFO](CT_USER_DOMAIN_INFO.md) | `CT_DOMAIN_INFO_ID` |
| [PROT_AMENDMENT](PROT_AMENDMENT.md) | `CT_DOMAIN_INFO_ID` |

