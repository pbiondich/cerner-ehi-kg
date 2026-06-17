# GS_MED_CLAIM

> Pharmacy benefit claims reported by the payer or pharmacy.

**Description:** Grid Services - Medical Claims  
**Table type:** ACTIVITY  
**Primary key:** `GS_MED_CLAIM_ID`  
**Columns:** 51  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The internal value for the report order catalog item. |
| 6 | `CATALOG_CKI` | VARCHAR(250) | NOT NULL |  | Knowledge index of the order catalog entry that corresponds to the claimed product.If CATALOG_CD is NULL, might contain CKI id that does not correspond to an order catalog entry; e.g., the claim corresponds to a known drug in the Multum vocabulary that is not in the order catalog. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Timestamp when the entry was first entered into the database. (The UPDT_DT_TM is when the row was entered into the table.) |
| 9 | `DAYS_SUPPLY_QTY` | DOUBLE |  |  | The number of days the product will last. |
| 10 | `DISPENSE_QTY` | DOUBLE | NOT NULL |  | Product-level order catalog synonym entry that corresponds to the "claim"ed product. |
| 11 | `DOSAGE_INSTRUCTIONS` | VARCHAR(1000) |  |  | The dosage instructions for the claim, detailing the administration of the product in doses. |
| 12 | `EXT_PHARMACY_IDENT` | VARCHAR(50) |  |  | The identifier of the external pharmacy where the claim might be dispensed. |
| 13 | `EXT_PHARMACY_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of pharmacy identifier. |
| 14 | `EXT_PRESCRIBER_IDENT` | VARCHAR(200) |  |  | The external identifier of the person prescribing the claim. |
| 15 | `EXT_PRESCRIBER_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of the identifier of the person prescribing the claim. |
| 16 | `EXT_PRODUCT_IDENT` | VARCHAR(50) |  |  | The Identifier of the product dispensed in this claim. |
| 17 | `EXT_PRODUCT_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of the product identifier (NDC, HIN, Etc.) |
| 18 | `FILL_NUMBER_TXT` | VARCHAR(50) |  |  | The fill number for the medication dispense, 0 being the initial fill. |
| 19 | `GS_MED_CLAIM_ID` | DOUBLE | NOT NULL | PK | Identifies a pharmacy benefit claim reported by the payer or pharmacy. |
| 20 | `LAST_FILL_DT_TM` | DATETIME |  |  | The date the patient last refilled the claim. |
| 21 | `OBTAINED_DT_TM` | DATETIME |  |  | The date when the claim was obtained from the external services. |
| 22 | `ORIGINAL_REFILLS_TXT` | VARCHAR(50) |  |  | The original number of refills for the claim. |
| 23 | `ORIG_GS_MED_CLAIM_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the original claim that this claim was renewed from. If it is the original claim this ID will be 0. |
| 24 | `PAYER_NAME` | VARCHAR(100) |  |  | The name of the payer. |
| 25 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | The millennium identifier of the organization responsible for paying the claim expenses. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | It is the person for whom the pharmacy benefit claim is reported on by the payer or pharmacy. |
| 27 | `PHARMACY_IDENTIFIER` | VARCHAR(100) | NOT NULL |  | Identifier for the pharmacy |
| 28 | `PHARMACY_NAME` | VARCHAR(100) | NOT NULL |  | Name of dispensing pharmacy that submitted the claim. (As transmitted with the claim) |
| 29 | `PRESCRIBER_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the physician that prescribed the "claim"ed product. |
| 30 | `PRESCRIBER_NAME` | VARCHAR(135) | NOT NULL |  | Name of the physician that prescribed the "claim"ed product. (As received in the claim) |
| 31 | `PRESCRIBER_ORDER_NUMBER` | VARCHAR(100) |  |  | Identifies the prescriber order number. |
| 32 | `PRESCRIPTION_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the health plan the claim was created from. |
| 33 | `PRN_REFILL_FLAG` | DOUBLE | NOT NULL |  | Indicates if refills are to be given as needed. Values: 0 - Unknown, 1 - Not PRN, 2 - PRN. |
| 34 | `PRODUCT_DESCRIPTION` | VARCHAR(250) | NOT NULL |  | Describes the product that was the subject of the claim. (As transmitted with the claim) |
| 35 | `PRODUCT_DOSE_TXT` | VARCHAR(100) |  |  | The product dose description. |
| 36 | `PRODUCT_SYNONYM_CKI` | VARCHAR(250) | NOT NULL |  | Knowledge Index of the order catalog synonym that corresponds to the claimed product, at the product level. If the SYNONYM_ID is null, this column might be populated with a CKI id that does not correspond to an order catalog entry. |
| 37 | `PRODUCT_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Product-level order catalog synonym entry that corresponds to the claimed product. |
| 38 | `RECEIVED_QTY_TXT` | VARCHAR(50) |  |  | The received quantity display. |
| 39 | `RECEIVED_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | The claim's received quantity unit. |
| 40 | `REFILL_NBR` | DOUBLE | NOT NULL |  | Indicates whether this claim was based on a refill of an original prescription, and which refill this is. (0 if this is the first claim on the prescription). NOTE: This column has been replaced with Fill_Number_Txt and is no longer supported. |
| 41 | `REFILL_NBR_NOT_APPLIED_IND` | DOUBLE | NOT NULL |  | Indicates if the refilled number was applied or not. 0 - The refill number applies. 1 - The refill number does not apply. |
| 42 | `REMAINING_REFILLS_TXT` | VARCHAR(50) |  |  | The remaining number of refills for the claim. |
| 43 | `SERVICE_DT_TM` | DATETIME | NOT NULL |  | Date of service associated with the claim. |
| 44 | `SOURCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Describes the source type of the claim. The value is 0 if it is unknown, 1 if it is a payer, 2 if it is a pharmacy. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the claim. This number will increase each time a claim is renewed. A new claim will have a version of 0. |
| 51 | `WRITTEN_DT_TM` | DATETIME |  |  | The date the prescription was written for the associated claim. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ORIG_GS_MED_CLAIM_ID` | [GS_MED_CLAIM](GS_MED_CLAIM.md) | `GS_MED_CLAIM_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRESCRIBER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRESCRIPTION_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PRODUCT_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [GS_MED_CLAIM](GS_MED_CLAIM.md) | `ORIG_GS_MED_CLAIM_ID` |

