# UKRWH_CDS_PROCEDURE

> Contains CDS Procedure details at the level of a Procedure relating to a CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Procedure  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 7 | `PRIMARY_PROCEDURE_DT_TM` | DATETIME |  |  | This is the Clinical Intervention Date of the PRIMARY OPERATION (OPCS-4). Primary Procedure Date is an ACTIVITY DATE where the ACTIVITY DATE TIME TYPE is National Code 41 'Primary Procedure Date'. Clinical Intervention Date is an ACTIVITY DATE were ACTIVITY DATE TIME TYPE is National Code 34 'Clinical Intervention Date'. |
| 8 | `PROCEDURE_CD_TXT` | VARCHAR(4) |  |  | Primary' is a classification of PATIENT PROCEDURE CODING SIGNIFICANCE of INTERVENTION CLASSIFICATION ASSOCIATION for the coding of an OPERATIVE PROCEDURE. |
| 9 | `PROCEDURE_MOHPR_ENTRY_IDENT` | VARCHAR(12) |  |  | The PROFESSIONAL REGISTRATION ENTRY IDENTIFIER of the CARE PROFESSIONAL carrying out a Patient Procedure of MAIN Operating healthcare professional. |
| 10 | `PROCEDURE_MOHPR_ISSUE_NHS` | VARCHAR(2) |  |  | PROFESSIONAL REGISTRATION ISSUER CODE is the same as attribute PROFESSIONAL REGISTRATION BODY CODE of MAIN Operating healthcare professional. |
| 11 | `PROCEDURE_RAPR_ENTRY_IDENT` | VARCHAR(12) |  |  | PROFESSIONAL REGISTRATION ISSUER CODE is the same as attribute PROFESSIONAL REGISTRATION BODY CODE of the carrying out a Patient Procedure of responsible anaesthetist. |
| 12 | `PROCEDURE_RAPR_ISSUE_NHS` | VARCHAR(2) |  |  | An indication of whether a PATIENT DIAGNOSIS was already present when the PATIENT started a Hospital Provider Spell of the carrying out a Patient Procedure of responsible anaesthetist. |
| 13 | `PROCEDURE_SCHEME_NHS` | VARCHAR(2) |  |  | This is used in the Clinical Activity Group of the CDS to denote the scheme basis of an Intervention, Operation or A&E Treatment. |
| 14 | `PROCEDURE_SEQ` | DOUBLE |  |  | A Number given to a procedure other than the PRIMARY PROCEDURE (OPCS), carried out and recorded for CDS or HES purposes. For CDS purposes it is recommended that multiple Procedures are recorded and the CDS-XML Message (CDS Version 6 onwards) has been designed to carry as many Procedures as required. |
| 15 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 16 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 17 | `UKRWH_CDS_PROCEDURE_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds procedure table. It is an internal system assigned number. |
| 18 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

