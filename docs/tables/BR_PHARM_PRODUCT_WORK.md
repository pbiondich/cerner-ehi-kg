# BR_PHARM_PRODUCT_WORK

> This table contains the client's pharmacy items from their legacy system

**Description:** Bedrock Pharmacy Product Work  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQUISITION_COST` | DOUBLE | NOT NULL |  | Acquisition cost for the product |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `CHARGE_NBR` | VARCHAR(200) |  |  | Charge identifier for the product |
| 4 | `DESCRIPTION` | VARCHAR(60) | NOT NULL |  | Description of the product |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility with which the product is associated |
| 6 | `MATCH_IND` | DOUBLE | NOT NULL |  | indicates if this product has been matched to a Multum item |
| 7 | `MATCH_NDC` | VARCHAR(11) |  |  | NDC of the item to which product was matched |
| 8 | `MATCH_OPTION` | DOUBLE | NOT NULL |  | data option chosen during the match |
| 9 | `NDC` | VARCHAR(11) | NOT NULL |  | National Drug Code of the product |
| 10 | `UBC_IDENT` | VARCHAR(200) |  |  | unit based cabinet identifier for the product |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

