# OSM_DEFAULTS

> Outreach Services Managment Defaults

**Description:** OSM DEFAULTS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_FLAG` | DOUBLE |  |  | This determines if AGE is required in Requisition Order Entry. |
| 2 | `BIRTH_DATE_FLAG` | DOUBLE |  |  | This determines if BIRTHDATE is required in Requisition Order Entry. |
| 3 | `BIRTH_TIME_FLAG` | DOUBLE |  |  | This determines if BIRTH TIME is required in Requisition Order Entry. |
| 4 | `DFLT_HP_ADDR_TYPE_CD` | DOUBLE | NOT NULL |  | Address type that should be automatically selected for the selected health plan. |
| 5 | `DX_FLAG` | DOUBLE |  |  | This determines if DIAGNOSIS is required in Requisition Order Entry. |
| 6 | `EEM_ABN_CHECK_IND` | DOUBLE |  |  | Determines if EEM ABN checking will be used. |
| 7 | `FINANCIAL_ASSIGNMENT_FLAG` | DOUBLE |  |  | Indicator flag to determine financial assessibility. |
| 8 | `FINANCIAL_NUMBER_FLAG` | DOUBLE |  |  | This determines if FINANCIAL NUMBER is required in Requisition Order Entry. |
| 9 | `FIRST_NAME_FLAG` | DOUBLE |  |  | This determines if FIRST NAME is required in Requisition Order Entry. |
| 10 | `LAB_ORG_ID` | DOUBLE | NOT NULL | FK→ | The default organization of the laboratory. Used for printing laboratory name and address on reports. |
| 11 | `LANGUAGE_FLAG` | DOUBLE |  |  | This determines if LANGUAGE is required in Requisition Order Entry. |
| 12 | `MIDDLE_NAME_FLAG` | DOUBLE |  |  | This determines if MIDDLE NAME is required in Requisition Order Entry. |
| 13 | `ORDER_COMMENT_FLAG` | DOUBLE |  |  | This determines what ORDER COMMENT type(s) are available in Requisition Order Entry. |
| 14 | `ORDER_DONOR_PRODUCT_IND` | DOUBLE |  |  | This determines if ORDERs of DONOR or PRODUCTS is allowed in Requisition Order Entry. [0 - no, 1- yes] |
| 15 | `PHONE_FLAG` | DOUBLE |  |  | This determines if PHONE is required in Requisition Order Entry. |
| 16 | `PHYS_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Physician alias type code from code set 320. |
| 17 | `PHYS_FILTERED_ALIAS_IND` | DOUBLE |  |  | Physician filtered alias indicator. This setting is no longer used. |
| 18 | `PHYS_ORG_FILTER_IND` | DOUBLE |  |  | This determines if PHYSICIANS are filter by client in Requisition Order Entry. AGE required? [0 = no,1 = yes] |
| 19 | `RACE_FLAG` | DOUBLE |  |  | This determines if RACE is required in Requisition Order Entry. |
| 20 | `REG_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | This determines the CONTRIBUTOR SYSTEM for encounter match and tag in Requisition Order Entry. |
| 21 | `REQUISITION_IND` | DOUBLE |  |  | This determines if REQUISITION NUMBER is USED in Requisition Order Entry. [0 - no,1 - yes] |
| 22 | `ROE_ADDON_LIMIT_DAYS` | DOUBLE |  |  | The limited days of which will allow ROE to load orders for addon. |
| 23 | `ROE_CANCEL_ORDER` | VARCHAR(100) |  |  | The default setting for cancel orders in ROE. |
| 24 | `ROE_DEMOGRAPHICS` | VARCHAR(100) |  |  | Requisition Order Entry patient demographics. |
| 25 | `ROE_DUAL_ORDER` | VARCHAR(100) |  |  | This stores Requisition Order Entry ordered procedures for dual entry. |
| 26 | `ROE_DUAL_REGISTRATION` | VARCHAR(100) |  |  | This stores Requisition Order Entry ordered procedures for dual entry registration. |
| 27 | `ROE_ENCNTR_SEARCH` | VARCHAR(100) |  |  | Requisition Order Entry Encounter Alias Search Default. |
| 28 | `ROE_MODIFY_ORDER` | VARCHAR(100) |  |  | This stores modified Requisition Order Entry ordered procedures. |
| 29 | `ROE_MODIFY_REGISTRATION` | VARCHAR(100) |  |  | This stores modified Requisition Order Entry ordered procedures for registration. |
| 30 | `SEX_FLAG` | DOUBLE |  |  | This determines if SEX is required in Requisition Order Entry. |
| 31 | `SSN_FLAG` | DOUBLE |  |  | This determines if SOCIAL SECURITY NUMBER is required in Requisition Order Entry. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `VOC_IND` | DOUBLE | NOT NULL |  | Flag to enable VOC use in OSM Requisition Order Entry. 0 = disabled 1 = enabled |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAB_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

