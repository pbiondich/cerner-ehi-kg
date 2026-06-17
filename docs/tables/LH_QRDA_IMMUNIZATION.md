# LH_QRDA_IMMUNIZATION

> This table is used to store elements that are used to create the Immunization Section in the body of a QRDA file for submission

**Description:** LH_QRDA_IMMUNIZATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOSE_QUANTITY` | VARCHAR(50) |  |  | Units of medication to take per administration |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 7 | `LH_QRDA_IMMUNIZATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_IMMUNIZATION table. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. |
| 9 | `MEDICATION_DT_TM` | DATETIME |  |  | Indicates the actual or intended time of administration/dispensing of medication |
| 10 | `MED_ID` | DOUBLE | NOT NULL |  | Unique medication id |
| 11 | `MED_STATUS_CODE` | VARCHAR(50) |  |  | Represents the status of the medication. |
| 12 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 13 | `NEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time when the negation was recorded |
| 14 | `NEG_PRODUCT_CODE` | VARCHAR(50) |  |  | CMS code that describes the negation |
| 15 | `NEG_PRODUCT_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system from which neg_product_code was derived from |
| 16 | `NEG_PRODUCT_DISPLAY` | VARCHAR(500) |  |  | Text description of the negation |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Immunization section is related (i.e. lh_qrda_pqrs_id) |
| 18 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 19 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Immunization section is related (i.e. LH_QRDA_PQRS) |
| 20 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 21 | `PRODUCT_CODE` | VARCHAR(50) |  |  | Code that describes the product/medication |
| 22 | `PRODUCT_CODE_SYSTEM` | VARCHAR(50) |  |  | Code system from which product_cd was derived from |
| 23 | `PRODUCT_DISPLAY` | VARCHAR(500) |  |  | Text description of the product |
| 24 | `PRODUCT_FULL_DISPLAY` | VARCHAR(500) |  |  | Full length text description of the product |
| 25 | `ROUTE_CODE` | VARCHAR(50) |  |  | Code describing the route of administration |
| 26 | `SUPPLY_IND` | DOUBLE |  |  | Indicates whether the activity is a SubstanceAdministration (medication activity) or Supply (supply activity). 0 indicates medication activity and 1 indicates supply activity |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 30 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

