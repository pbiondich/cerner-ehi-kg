# INFOSCAN_ORG

> InfoScan Organization Table

**Description:** InfoScan Organization  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDR1` | VARCHAR(40) |  |  | Address 1Column |
| 2 | `CITY` | VARCHAR(40) |  |  | cityColumn |
| 3 | `FORMULARY_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | formulary identifierColumn |
| 4 | `INFOSCAN_ORG_IDENTIFIER` | VARCHAR(15) | NOT NULL |  | InfoScan Organization IdentifierColumn |
| 5 | `INJECT_DRUG_CVRG_FLAG` | DOUBLE |  |  | injectable drug coverage flagColumn |
| 6 | `NAME` | VARCHAR(80) |  |  | nameColumn |
| 7 | `NEW_APP_DRUG_CVRG_FLAG` | DOUBLE |  |  | newly approved drug coverageColumn |
| 8 | `NON_FORMU_CVRG_FLAG` | DOUBLE |  |  | non formulary drug coverage flagColumn |
| 9 | `OC_CVRG_FLAG` | DOUBLE |  |  | oral contraceptive coverage flagColumn |
| 10 | `OTC_CVRG_FLAG` | DOUBLE |  |  | OTC coverage flagColumn |
| 11 | `POLICY_BRAND_INTERCHG_FLAG` | DOUBLE |  |  | policy brand interchange flagColumn |
| 12 | `POLICY_BRAND_REIMBURSE_FLAG` | DOUBLE |  |  | policy brand reimburse flagColumn |
| 13 | `POLICY_GENERIC_DRUG_FLAG` | DOUBLE |  |  | policy generic drug flagColumn |
| 14 | `POLICY_UNLISTED_DRUG_FLAG` | DOUBLE |  |  | policy unlisted drug flagColumn |
| 15 | `SMOKE_CESS_CVRG_FLAG` | DOUBLE |  |  | smoking cessation coverage flagColumn |
| 16 | `STATE` | CHAR(2) |  |  | stateColumn |
| 17 | `TIER_FLAG` | DOUBLE |  |  | tier flagColumn |
| 18 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of Healthcare Organization or Plan. 1 - HMO, 2 - PPO, 3 - Insurer, 4 - Employer, 5 - PBM, 6 - POS, 7 - Medicaid, 8 - Medical Group |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `XPRMNTL_DRUG_CVRG_FLAG` | DOUBLE |  |  | experimental drug coverage flagColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

