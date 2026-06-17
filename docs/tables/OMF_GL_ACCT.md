# OMF_GL_ACCT

> omf_gl_acct

**Description:** Contains the OMF General Ledger account data.  
**Table type:** ACTIVITY  
**Primary key:** `OMF_GL_ACCT_ID`  
**Columns:** 53  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_CODE` | VARCHAR(50) |  |  | An abbreviation for an account |
| 2 | `ACCT_DESC` | VARCHAR(100) |  |  | A descriptive name that identifies the nature of the transactions that are posted to the general ledger. |
| 3 | `ACCT_TYPE` | VARCHAR(100) |  |  | The name of a grouping of like accounts in a general ledger. |
| 4 | `ACCT_TYPE_CODE` | VARCHAR(50) |  |  | The abbreviation for an account type. |
| 5 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center to which the general ledger account belongs. |
| 6 | `COST_CENTER_CODE` | VARCHAR(50) |  |  | The abbreviation for a cost center. |
| 7 | `COST_CENTER_DESC` | VARCHAR(100) |  |  | The description of a cost center. |
| 8 | `DEPT_CD` | DOUBLE | NOT NULL |  | The department to which a general ledger account belongs |
| 9 | `DEPT_CODE` | VARCHAR(50) |  |  | The abbreviation for the department. |
| 10 | `DEPT_DESC` | VARCHAR(100) |  |  | The description of the department. |
| 11 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility to which a general ledger account belongs. |
| 12 | `FACILITY_CODE` | VARCHAR(50) |  |  | The abbreviation for the facility. |
| 13 | `FACILITY_DESC` | VARCHAR(100) |  |  | The description of the facility |
| 14 | `FUND_CODE` | VARCHAR(50) |  |  | The abbreviation for the fund. |
| 15 | `FUND_DESC` | VARCHAR(100) |  |  | The fund to which a general ledger account belongs. |
| 16 | `GL_ACCT_IDENT` | VARCHAR(255) |  |  | The concatenation of all component parts that identify a general ledger account. |
| 17 | `GL_ACCT_IDENT_CODE` | VARCHAR(100) |  |  | The abbreviation for a GL account ID. |
| 18 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | The institution to which a general ledger account belongs. |
| 19 | `INSTITUTION_CODE` | VARCHAR(50) |  |  | The abbreviation for the institution. |
| 20 | `INSTITUTION_DESC` | VARCHAR(100) |  |  | The description for the institution. |
| 21 | `OMF_GL_ACCT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the omf_gl_acct table. |
| 22 | `PROJECT_CODE` | VARCHAR(50) |  |  | The abbreviation for the project. |
| 23 | `PROJECT_DESC` | VARCHAR(100) |  |  | The project to which a general ledger account belongs. |
| 24 | `SMRY_GRP10_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 25 | `SMRY_GRP10_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 26 | `SMRY_GRP1_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 27 | `SMRY_GRP1_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 28 | `SMRY_GRP2_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 29 | `SMRY_GRP2_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 30 | `SMRY_GRP3_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 31 | `SMRY_GRP3_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 32 | `SMRY_GRP4_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 33 | `SMRY_GRP4_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 34 | `SMRY_GRP5_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 35 | `SMRY_GRP5_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 36 | `SMRY_GRP6_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 37 | `SMRY_GRP6_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 38 | `SMRY_GRP7_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 39 | `SMRY_GRP7_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 40 | `SMRY_GRP8_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 41 | `SMRY_GRP8_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 42 | `SMRY_GRP9_CODE` | VARCHAR(50) |  |  | Client defined grouping of accounts. |
| 43 | `SMRY_GRP9_DESC` | VARCHAR(100) |  |  | Client defined grouping of accounts. |
| 44 | `SUB_ACCT1_CODE` | VARCHAR(50) |  |  | The abbreviation for the sub account. |
| 45 | `SUB_ACCT1_DESC` | VARCHAR(100) |  |  | A descriptive name that identifies the nature of transactions that are posted to the GL. |
| 46 | `SUB_ACCT2_CODE` | VARCHAR(50) |  |  | The abbreviation for the sub account. |
| 47 | `SUB_ACCT2_DESC` | VARCHAR(100) |  |  | A descriptive name that identifies the nature of transactions that are posted to the GL. |
| 48 | `SUB_ACCT3_CODE` | VARCHAR(50) |  |  | The abbreviation for the sub account. |
| 49 | `SUB_ACCT3_DESC` | VARCHAR(100) |  |  | A descriptive name that identifies the nature of transactions that are posted to the GL. |
| 50 | `SUB_ACCT4_CODE` | VARCHAR(50) |  |  | The abbreviation for the sub account. |
| 51 | `SUB_ACCT4_DESC` | VARCHAR(100) |  |  | A descriptive name that identifies the nature of transactions that are posted to the GL. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OMF_ACR_FACT](OMF_ACR_FACT.md) | `OMF_GL_ACCT_ID` |
| [OMF_BLS_FACT](OMF_BLS_FACT.md) | `OMF_GL_ACCT_ID` |
| [OMF_ICS_BDGT](OMF_ICS_BDGT.md) | `OMF_GL_ACCT_ID` |
| [OMF_ICS_FACT](OMF_ICS_FACT.md) | `OMF_GL_ACCT_ID` |

