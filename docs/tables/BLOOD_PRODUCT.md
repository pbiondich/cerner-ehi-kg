# BLOOD_PRODUCT

> Attributes that are specific to a blood product (as opposed to a derivative).

**Description:** Blood product  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTOLOGOUS_IND` | DOUBLE |  |  | Indicates whether this blood product is an autologous product. Indicates whether this product was donated by a person to be transfused at a later time. |
| 6 | `CUR_ABO_CD` | DOUBLE | NOT NULL |  | Current ABO group of this blood product, whether entered at the time it was received, or confirmed through testing. |
| 7 | `CUR_RH_CD` | DOUBLE | NOT NULL |  | The current Rh for this blood product, whether it was entered at time of receiving it or confirmed through testing (ex. "Pos", "Neg") |
| 8 | `CUR_VOLUME` | DOUBLE |  |  | Indicates the current volume for this blood product. Entered at the time it was received, and updated during any product modification. |
| 9 | `DIRECTED_IND` | DOUBLE |  |  | Indicates whether this blood product was donated as a directed product, intended for a designated recipient. |
| 10 | `DONOR_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `DRAWN_DT_TM` | DATETIME |  |  | This field contains the date and time the product was drawn from the donor. It is only filled out if the site has the Cerner Blood Bank Donor module and the product was drawn in house. |
| 12 | `LOT_NBR` | VARCHAR(25) |  |  | The lot number of the bag of the blood product. |
| 13 | `ORIG_EXPIRE_DT_TM` | DATETIME |  |  | The expiration date and time that was originally entered for the blood product at the time it was received into the blood bank. |
| 14 | `ORIG_LABEL_ABO_CD` | DOUBLE | NOT NULL |  | The ABO of the blood product as it was originally labeled when it was received into the blood bank. |
| 15 | `ORIG_LABEL_RH_CD` | DOUBLE | NOT NULL |  | The RH of the blood product as it was originally labeled when it was received into the blood bank (ex. "Pos", "Neg"). |
| 16 | `ORIG_VOLUME` | DOUBLE |  |  | The volume of the blood product as it was when it was originally entered into the blood bank. |
| 17 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Indicates the exact type of blood product, e.g., "Red Blood Cells CPDA1", "Fresh Frozen Plasma", etc. |
| 18 | `PRODUCT_ID` | DOUBLE | NOT NULL | PK FK→ | The ID of the product from the PRODUCT table to uniquely identify this blood product. |
| 19 | `SEGMENT_NBR` | VARCHAR(25) |  |  | The segment number of the blood product as entered from the bag at the time it was received into the blood bank. |
| 20 | `SUPPLIER_PREFIX` | CHAR(5) |  |  | This column may be empty. It represents the FDA originating supplier prefix on this bag of blood, i.e., the donor center where the blood was originally drawn from the blood donor. An example is "09", which becomes part of the product number, e.g., "09G12345". |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DONOR_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ABO_TESTING](ABO_TESTING.md) | `PRODUCT_ID` |

