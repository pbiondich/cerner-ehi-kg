# LEGAL_AUTHORITY

> Stores information on behavioral health legal authority build models.

**Description:** Legal Authority  
**Table type:** REFERENCE  
**Primary key:** `LEGAL_AUTHORITY_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMITMENT_PERIOD` | DOUBLE | NOT NULL |  | A number indicating the length of commitment period. |
| 2 | `COMMITMENT_PERIOD_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the unit qualifier (days, hours, etc.) for the commitment period. |
| 3 | `COMMITMENT_TYPE_CD` | DOUBLE | NOT NULL |  | A code indicating the type of commitment. |
| 4 | `COURT_ORDER_NAME` | VARCHAR(100) | NOT NULL |  | A code indicating the commitment order name. |
| 5 | `LA_END_DT_TM` | DATETIME | NOT NULL |  | The end date of this legal court order. |
| 6 | `LA_START_DT_TM` | DATETIME | NOT NULL |  | The start date of this legal court order. |
| 7 | `LEGAL_AUTHORITY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LEGAL_AUTHORITY table. |
| 8 | `LEGAL_REFERENCE_CD` | DOUBLE | NOT NULL |  | A code indicating the reference to the legal code permitting commitment. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `SSA_INMATE_CD` | DOUBLE | NOT NULL |  | A code indicating the Social Security inmate code for the commitment. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WEEK_DAYS_ONLY_IND` | DOUBLE |  |  | An indicator identifying if the length of commitment period only considers week days. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ENCNTR_LEGAL_AUTH_RELTN](ENCNTR_LEGAL_AUTH_RELTN.md) | `LEGAL_AUTHORITY_ID` |
| [ENCNTR_LEGAL_AUTH_R_HIST](ENCNTR_LEGAL_AUTH_R_HIST.md) | `LEGAL_AUTHORITY_ID` |

