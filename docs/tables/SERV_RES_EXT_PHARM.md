# SERV_RES_EXT_PHARM

> Serv_res_ext_pharm - Stores pharmacy specific attributes of a Service Resource.

**Description:** SERV RES EXT PHARM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTM_DSPNS_MACHN_CD` | DOUBLE | NOT NULL |  | The type of the Service Resource. |
| 2 | `COST_BASIS_CD` | DOUBLE | NOT NULL |  | The default cost basis code for the service resource. |
| 3 | `DEA_NUMBER` | VARCHAR(100) |  |  | ALPHANUMERIC STRING FOR DEA NUMBER FOR THIS SERVICE RESOURCE |
| 4 | `DEFAULT_ERX_PHARMACY_IND` | DOUBLE | NOT NULL |  | Indicates that this service resource is the default resource used for new electronic prescriptions when multiple service resources have a duplicate pharmacy identifier (ie. NABP or ERx Pharmacy ID) |
| 5 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | DEFAULT DISPENSE PRIORITY FOR THIS SERVICE RESOURCE |
| 6 | `DOWNTIME_RANGE_ID` | DOUBLE | NOT NULL | FK→ | DOWN TIME RANGE INDICATOR FOR THIS SERVICE RESOURCE USED FOR DOWNTIME PRESCRIPTION NUMBER ASSIGNMENT. |
| 7 | `ESO_DOSE_MSG_IND` | DOUBLE | NOT NULL |  | ESO Dose Message Indicator |
| 8 | `ESO_INGRED_IND` | DOUBLE | NOT NULL |  | ESO Ingredient Indicator |
| 9 | `ESO_TPN_CPMD_IND` | DOUBLE | NOT NULL |  | ESO TPN Compound Indicator |
| 10 | `FLOORSTOCK_IND` | DOUBLE |  |  | Indicates the resource is a floorstock resource, i.e., resource is associated with or located on a patient care location and not a pharmacy location. |
| 11 | `INV_LOCATION_CD` | DOUBLE | NOT NULL |  | Identifies the related inventory location for a primary service resource. |
| 12 | `NABP_NUMBER` | VARCHAR(100) |  |  | ALPHA NUMERIC STRING FOR NABP NUMBER FOR THIS SERVICE RESOURCE |
| 13 | `OTC_SALES_TAX` | DOUBLE |  |  | OVER THE COUNTER - SALES TAX |
| 14 | `PAT_CARE_LOC_IND` | DOUBLE |  |  | Indicates this resource is located in a nurse unit rather than in the pharmacy. |
| 15 | `PHARMACY_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the Pharmacy Service Resource Type defined in NCPDP Pharmacy service resource type code set. |
| 16 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | If the service resource is a pharmacy section or subsection, indicates the type of pharmacy from code_set 4500. Currently home infusion, long term care, inpatient, mail order, and retail. |
| 17 | `PHARM_CATEGORY_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 18 | `PROVIDER_TYPE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 19 | `RXNBR_CD` | DOUBLE | NOT NULL |  | RX Number Code - CODE VALUE FROM CODE SET 4550 |
| 20 | `RX_CHARGE_IND` | DOUBLE |  |  | ** OBSOLETE ** NO LONGER USED ** |
| 21 | `RX_IN_CHARGE_ID` | DOUBLE | NOT NULL |  | PRSNL ID OF PHARMACIST-IN-CHARGE FOR THIS SERVICE RESOURCE |
| 22 | `SALES_TAX` | DOUBLE |  |  | SALES TAX FOR THIS SERVICE RESOURCE |
| 23 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique internal identifier for this service resource |
| 24 | `STATE_CONTROL_NUMBER` | CHAR(100) |  |  | ALPHANUMERIC STRING FOR STATE LICENSE NUMBER FOR THIS SERVICE RESOURCE |
| 25 | `STATE_LICENSE_NUMBER` | VARCHAR(100) |  |  | ALPHANUMERIC STRING FOR STATE LICENSE NUMBER FOR THIS SERVICE RESOURCE |
| 26 | `TAX_NUMBER` | VARCHAR(100) |  |  | ALPHANUMERIC STRING FOR TAX NUMBER FOR THIS SERVICE RESOURCE |
| 27 | `TRACK_NBR_CD` | DOUBLE | NOT NULL |  | Track Number Code - CODE VALUE FROM CODE SET 4504 |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOWNTIME_RANGE_ID` | [PHARMACY_RANGE](PHARMACY_RANGE.md) | `RANGE_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

