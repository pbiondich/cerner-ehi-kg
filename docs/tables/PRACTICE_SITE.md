# PRACTICE_SITE

> Defines a practice site and its address and phone.

**Description:** Practice Site  
**Table type:** REFERENCE  
**Primary key:** `PRACTICE_SITE_ID`  
**Columns:** 15  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLOSE_DT_TM` | DATETIME |  |  | Date time defines when the practice site is or will go out of service. |
| 2 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 3 | `OPEN_DT_TM` | DATETIME |  |  | Date and time when the site is going to be available for service. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the organization table. |
| 5 | `PRACTICE_SITE_DISPLAY` | VARCHAR(100) | NOT NULL |  | Value of the ORG_NAME from ORGANIZATION or display of the LOCATION_TYPE_CD from LOCATION. |
| 6 | `PRACTICE_SITE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the practice_site table. |
| 7 | `PRACTICE_SITE_SYSTEM_CD` | DOUBLE | NOT NULL |  | Code value which explains whether the site is internal, or external, etc. |
| 8 | `PRIMARY_ENTITY_ID` | DOUBLE | NOT NULL |  | Entity ID which will be used to get the Address and Phone for a practice site. |
| 9 | `PRIMARY_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Entity Name which will be used to the the Address and Phone for a practice site. |
| 10 | `SCHEDULE_SYSTEM_TYPE_CD` | DOUBLE | NOT NULL |  | Code value representing the scheduling system being used for the practice site, like Millennium Revenue Cycle, Millennium ESM |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [PRACTICE_SITE_MSG_ROUTING](PRACTICE_SITE_MSG_ROUTING.md) | `PRACTICE_SITE_ID` |
| [PRACTICE_SITE_RELTN](PRACTICE_SITE_RELTN.md) | `PRACTICE_SITE_ID` |
| [PRACTICE_SITE_TYPE_RELTN](PRACTICE_SITE_TYPE_RELTN.md) | `PRACTICE_SITE_ID` |
| [PRAC_SITE_REF_APPT_TYPE](PRAC_SITE_REF_APPT_TYPE.md) | `PRACTICE_SITE_ID` |
| [PRAC_SITE_SPECIALTY_RELTN](PRAC_SITE_SPECIALTY_RELTN.md) | `PRACTICE_SITE_ID` |
| [REFERRAL](REFERRAL.md) | `REFER_FROM_PRACTICE_SITE_ID` |
| [REFERRAL](REFERRAL.md) | `REFER_TO_PRACTICE_SITE_ID` |
| [REFERRAL_HIST](REFERRAL_HIST.md) | `REFER_FROM_PRACTICE_SITE_ID` |
| [REFERRAL_HIST](REFERRAL_HIST.md) | `REFER_TO_PRACTICE_SITE_ID` |

