# EPA_RECORD

> Stores Electronic Prior Authorization information

**Description:** Electronic Prior Authorization Record  
**Table type:** ACTIVITY  
**Primary key:** `EPA_RECORD_ID`  
**Columns:** 30  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHANGERX_MESSAGE_IDENT` | VARCHAR(2000) |  |  | CHANGE RX MESSAGE IDENTIFIER |
| 3 | `CHG_RX_FLAG` | DOUBLE | NOT NULL |  | A flag that denotes if a Change Response has ben triggered. Supported Values: 0-Unset, 1 - This PA Record expects a Response, 2- Change Rx Response has been triggered. |
| 4 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The Data Time when the PA was created |
| 6 | `DATA_ENTERER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The action personnel of the prior authorization. |
| 7 | `DISMISS_IND` | DOUBLE | NOT NULL |  | Indicates if the record has been dismissed by the provider 1 = yes / 0= no |
| 8 | `DRUG_IDENT` | VARCHAR(2000) |  |  | The NDC of the drug. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter id tied to the prior authorization. |
| 10 | `EPA_MEDICATION_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The blob that contains un-matched drug information from the external vendor. FK value from EPA_LONG_BLOB |
| 11 | `EPA_PATIENT_DEMOG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The blob that contains un-matched patient information from the external vendor. FK value from EPA_LONG_BLOB |
| 12 | `EPA_RECORD_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 13 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange ID. refers to interchange_id on the EEM_TRANSACTION table. That column is a unique index on the table not the PK. |
| 14 | `INTERCHANGE_SEQUENCE` | DOUBLE | NOT NULL |  | Order of the transactions as found in the INTERCHANGE_ID field. |
| 15 | `MEDICATION_BLOB_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use column EPA_MEDICATION_BLOB_ID |
| 16 | `ORDER_CATALOG_CKI` | VARCHAR(255) |  |  | The order catalog CKI |
| 17 | `ORDER_DESCRIPTION` | VARCHAR(2000) |  |  | The drug description of the order. This can be the ORDERED_AS_MNEMONIC for Prospective workflows and the DRUG_DESCRIPTION from the NCPDP transaction for Retrospective workflows. |
| 18 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization where the medication was prescribed. |
| 19 | `PATIENT_DEMOG_BLOB_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use column EPA_PATIENT_DEMOG_BLOB_ID |
| 20 | `PA_CASE_IDENT` | VARCHAR(2000) |  |  | The tracking Identifier assigned by the Payer as a unique reference to this prior authorization case |
| 21 | `PA_REF_IDENT` | VARCHAR(2000) | NOT NULL |  | The tracking identifier on all prior authorization request and response transactions that tie related prior authorization transactions. |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient who the EPA belongs to. |
| 23 | `PHARMACY_IDENT` | VARCHAR(2000) |  |  | The NCPDP Identifier of the Pharmacy |
| 24 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider who prescribed the medication. |
| 25 | `RELATED_ORDER_ID` | DOUBLE | NOT NULL |  | The order id related to the Prior Authorization. This can be the order id for an order or the projected order id for a proposed order |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_ENTERER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EPA_MEDICATION_BLOB_ID` | [EPA_LONG_BLOB](EPA_LONG_BLOB.md) | `EPA_LONG_BLOB_ID` |
| `EPA_PATIENT_DEMOG_BLOB_ID` | [EPA_LONG_BLOB](EPA_LONG_BLOB.md) | `EPA_LONG_BLOB_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EPA_ACTIVITY](EPA_ACTIVITY.md) | `EPA_RECORD_ID` |
| [EPA_AUTH_DETAIL](EPA_AUTH_DETAIL.md) | `EPA_RECORD_ID` |
| [EPA_ERROR_LOG](EPA_ERROR_LOG.md) | `EPA_RECORD_ID` |

