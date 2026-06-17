# IB_RX_REQ_DRUG

> Contains drug information for the prescription request on the inbound pharmacy request (i.e. prescribed, dispensed)

**Description:** Inbound Pharmacy Request Drug  
**Table type:** ACTIVITY  
**Primary key:** `IB_RX_REQ_DRUG_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPOUND_DRUG_DESC` | LONGBLOB |  |  | Multiple drug ingredient descriptions for a specific compound drug. |
| 2 | `DAYS_SUPPLY_NBR` | DOUBLE |  |  | The number of days that the drug is supposed to last. |
| 3 | `DISPENSE_AS_WRITTEN_CD` | DOUBLE | NOT NULL |  | Indicates whether or not the drug needs to be dispensed exactly as written or if it can be changed. |
| 4 | `DISPENSE_QTY` | DOUBLE |  |  | The amount of the drug to be dispensed. |
| 5 | `DISPENSE_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | The units associated with the dispense_qty. |
| 6 | `DRUG_DESCRIPTION_TXT` | VARCHAR(255) |  |  | The description of the drug that contains information such as Drug Name, Strength, and Dose. |
| 7 | `DRUG_SEQ` | DOUBLE | NOT NULL |  | Preserves the order the drug list was received from the pharmacy. |
| 8 | `IB_RX_REQ_DRUG_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the IB_RX_REQ_DRUG table. |
| 9 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL | FK→ | The inbound request for this drug. |
| 10 | `LAST_FILL_DATE_TXT` | VARCHAR(30) |  |  | ISO 8601 Date of last fill of prescription from pharmacy. Used with NCPDP Script 2017071 and higher specification. |
| 11 | `LAST_FILL_DT_TM` | DATETIME |  |  | The date on which the prescription was last filled. |
| 12 | `ORDER_DT_TM` | DATETIME |  |  | The date and time on which the drug was ordered. |
| 13 | `PHARM_COMMENT_TXT` | VARCHAR(255) |  |  | Comments from the sending pharmacy. |
| 14 | `PRN_IND` | DOUBLE | NOT NULL |  | Indicates if the drug can be taken as needed. |
| 15 | `PRODUCT_IDENTIFIER` | VARCHAR(255) |  |  | The drug that is on the incoming request. |
| 16 | `PRODUCT_SCHEDULE_FLAG` | DOUBLE | NOT NULL |  | The DEA schedules that controlled drugs are divided into based on their potential for abuse and physical and psychological dependence. |
| 17 | `PRODUCT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the product type for the drug. Values: 0 - Neither, 1 - Compound, 2 - Supply. |
| 18 | `PROD_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | The product type code that the drug is identified by. For example: NDC. From code set 11000. |
| 19 | `REF_ORDER_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 20 | `REMAINING_REFILL_QTY` | DOUBLE |  |  | The number of refills remaining on the prescription. |
| 21 | `RENEWAL_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field is the type_flag and not just used for renewals (badly named). Indicates the type of request for this drug. 1 indicates this is a prescribed drug. 2 indicates this is a dispensed drug. 3 indicates this is a requested drug. 4 indicates this is a preferred requested drug |
| 22 | `SPECIAL_INSTRUCTIONS_TXT` | VARCHAR(1000) |  |  | Text instructions received with the incoming request. |
| 23 | `SYNONYM_ID` | DOUBLE |  | FK→ | This field corresponds to a matched order's synonym_id for the requested product identifier of the drug. This will be 0 if unable to match the product identifier or if a product identifier is not specified. This implies the drug will be free-text. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `WRITTEN_DATE_TXT` | VARCHAR(30) |  |  | ISO 8601 Date the prescription was written by the physician. Used with NCPDP Script 2017071 and higher specification. |
| 30 | `ZERO_REFILLS_SPECIFIED_IND` | DOUBLE | NOT NULL |  | Indicates whether the pharmacy actually specified zero refills. 1 indicates that they did explicitly specify that there were zero refills. 0 indicates that the pharmacy either did note refills or specified a number of refills greater than zero. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_ID` | [IB_RX_REQ](IB_RX_REQ.md) | `IB_RX_REQ_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [IB_RX_REQ_DIAGNOSIS](IB_RX_REQ_DIAGNOSIS.md) | `IB_RX_REQ_DRUG_ID` |

