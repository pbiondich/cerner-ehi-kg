# RESEARCH_ACCOUNT

> Table used to store research accounts and information about them

**Description:** Research Account  
**Table type:** REFERENCE  
**Primary key:** `RESEARCH_ACCOUNT_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_NBR` | CHAR(100) |  |  | Account Number associated with this research account |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DESCRIPTION` | CHAR(100) |  |  | Free-text description of the research account |
| 8 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type that should be defaulted if this research account is used. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NAME` | CHAR(40) |  |  | Name of the research account |
| 11 | `NAME_KEY` | CHAR(100) |  |  | Keyed attribute used internally and derived from the name attribute |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization that this research account is associated with. |
| 13 | `RESEARCH_ACCOUNT_ID` | DOUBLE | NOT NULL | PK | Primary Key Attribute |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ENCNTR_ORG_RELTN](ENCNTR_ORG_RELTN.md) | `RESEARCH_ACCOUNT_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `RESEARCH_ACCOUNT_ID` |
| [PROT_CRPC_BILLING](PROT_CRPC_BILLING.md) | `PROT_RESEARCH_ACCOUNT_ID` |

